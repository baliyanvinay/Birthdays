from django.shortcuts import render, reverse
from .models import Tab_Birthdays
from django.http import HttpResponseRedirect
from django.db.models.functions import Extract
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

# Create your views here.


def index(request):
    search_name = request.GET.get('search_name')
    if search_name:
        model_data = {
            "Birthdays": Tab_Birthdays.objects.filter(name__contains=search_name.capitalize()).order_by('dob_current_year'),
            "Birthday_today": Tab_Birthdays.objects.filter(dob_current_year=date.today())
        }
    else:
        '''
        dob_current_year__gt means comparision greater than the value on the right of the assignment operator
        '''
        model_data = {
            "Birthdays": Tab_Birthdays.objects.filter(dob_current_year__gte=date.today()).order_by('dob_current_year'),
            "Birthday_today": Tab_Birthdays.objects.filter(dob_current_year=date.today())
        }
    return render(request, template_name='list_birthdays/index.html', context=model_data)


def handle_request_object(request):
    if request.method == 'POST':  # getting data from HTML form via POST method
        name = request.POST['name']
        dob = request.POST['dob']
        # age=request.POST['age']
        '''
        Changed the dob format from str to date to get the date for the current year to display 
        upcoming birthdays in sorted way. Also dob is used to calculate the age of the person
        '''
        dob = datetime.strptime(dob, '%Y-%m-%d').date()
        dob_current_year = date(date.today().year, dob.month, dob.day)
        age = relativedelta(date.today(), dob).years
    return (name, dob, age, dob_current_year)


def add_new(request):
    name, dob, age, dob_current_year = handle_request_object(request)

    new_birthday = Tab_Birthdays(
        name=name, dob=dob, age=age, dob_current_year=dob_current_year)
    new_birthday.save()
    return render(request, template_name='list_birthdays/add_new.html')


def list_all(request):
    search_name = request.GET.get('search_name')
    if search_name:
        model_data = {
            "Birthdays": Tab_Birthdays.objects.filter(name__contains=search_name.capitalize()).order_by('dob_current_year')
        }
    else:
        model_data = {
            "Birthdays": Tab_Birthdays.objects.all().order_by('dob_current_year')
        }
    return render(request, template_name='list_birthdays/list_all.html', context=model_data)


def delete_birthday(request, delete_id):
    del_obj = Tab_Birthdays.objects.get(id=delete_id)
    del_obj.delete()

    # reloading the model_data after the delete has been called
    model_data = {
        "Birthdays": Tab_Birthdays.objects.all().order_by('dob_current_year')
    }
    return render(request, template_name='list_birthdays/list_all.html', context=model_data)


def edit_birthday(request, edit_id):
    edit_record = {
        "Edit_Birthday_display": Tab_Birthdays.objects.get(id=edit_id)
    }
    return render(request, template_name='list_birthdays/edit_birthday.html', context=edit_record)


def update_birthday(request, update_id):
    update_obj = Tab_Birthdays.objects.get(id=update_id)
    # below birthday details are the ones which user has posted via POST method in HTML
    updated_name, updated_dob, updated_age, updated_dob_current_year = handle_request_object(
        request)
    update_obj.name = updated_name
    update_obj.dob = updated_dob
    update_obj.age = updated_age
    update_obj.dob_current_year = updated_dob_current_year

    update_obj.save()
    '''
    Update the model object with the values that user has changed; Fetch the latest data from 
    model and pass it to list_birthdays/list_all.html
    '''

    model_data = {
        "Birthdays": Tab_Birthdays.objects.all().order_by('dob_current_year')
    }
    return render(request, template_name='list_birthdays/list_all.html', context=model_data)

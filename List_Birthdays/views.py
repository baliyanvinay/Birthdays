from django.shortcuts import render, reverse
from .models import Tab_Birthdays
from django.http import HttpResponseRedirect
from django.db.models.functions import Extract
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

# Create your views here.
def index(request):
    search_name=request.GET.get('search_name')
    if search_name:
        model_data={
        "Birthdays": Tab_Birthdays.objects.filter(name=search_name.capitalize()),
        "Birthday_today": Tab_Birthdays.objects.filter(dob_current_year=date.today())
        }
    else:
        '''
        dob_current_year__gt means comparision greater than the value on the right of the assignment operator
        '''
        model_data={
            "Birthdays": Tab_Birthdays.objects.filter(dob_current_year__gte=date.today()).order_by('dob_current_year'),
            "Birthday_today": Tab_Birthdays.objects.filter(dob_current_year=date.today())
        }   
    return render(request, template_name='list_birthdays/index.html', context=model_data)

def add_new(request):
    if request.method == 'POST': #getting data from HTML form via POST method
        name=request.POST['name']
        dob=request.POST['dob']
        #age=request.POST['age']
        '''
        Changed the dob format from str to date to get the date for the current year to display 
        upcoming birthdays in sorted way. Also dob is used to calculate the age of the person
        '''
        dob=datetime.strptime(dob, '%Y-%m-%d').date()
        dob_current_year=date(date.today().year, dob.month, dob.day)
        age=relativedelta(date.today(),dob).years

        new_birthday=Tab_Birthdays(name=name, dob=dob, age=age, dob_current_year=dob_current_year)
        new_birthday.save()
    return render(request, template_name='list_birthdays/add_new.html')
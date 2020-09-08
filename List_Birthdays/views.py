from django.shortcuts import render, reverse
from .models import Tab_Birthdays
from django.http import HttpResponseRedirect

# Create your views here.
def index(request, search_name):
    if search_name:
        print(search_name)
    model_data={
        "Birthdays": Tab_Birthdays.objects.all()
    }
    return render(request, template_name='list_birthdays/index.html', context=model_data)

def add_new(request):
    if request.method == 'POST': #getting data from HTML form via POST method
        name=request.POST['name']
        dob=request.POST['dob']
        age=request.POST['age']
        new_birthday=Tab_Birthdays(name=name, dob=dob, age=age)
        new_birthday.save()
    return render(request, template_name='list_birthdays/add_new.html')

def search(request, search_name):
    model_data={
        "Birthdays": Tab_Birthdays.objects.filter(name=search_name)
    }
    return render(request, template_name='list_birthdays/index.html', context=model_data)
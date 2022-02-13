from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import Employer , Employee


# Create your views here.
def index(request):
    r=Employer.objects.all()
    return render(request , 'index.html', {'r':r})


def list1(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
        pin = request.POST['pin']
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        pay = request.POST['pay']

        l= Employer(first_name= first_name , last_name= last_name , email= email , city= city , state= state , pin= pin, title= title , description= description , date= date, pay= pay )
        l.save()
        return redirect('/')

    else:
        first_name = ''
        last_name = ''
        email = ''
        city = ''
        state = ''
        pin = ''
        title = ''
        desription = ''        
        date = ''
        pay = ''
        l=''
    return render(request , 'list.html')

    


def employee_form(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
        pin = request.POST['pin']
        job = request.POST['job']
        experience = request.POST['experience']
        date = request.POST['date']
        salary = request.POST['salary']
        e = Employee(first_name= first_name , last_name= last_name , email= email , city= city , state= state , pin= pin, job= job , experience= experience , date= date, salary= salary )
        e.save()
        return redirect('thank')

    else:
        first_name = False
        last_name = False
        email = False
        city = False
        state = False
        pin = False
        job = False
        experience = False        
        date = False
        salary= False   

    return render(request , 'employee_form.html' , {'first_name':first_name , 'last_name':last_name , 'email':email , 'city':city , 'state':state , 'pin':pin , 'job':job , 'experience':experience , 'date':date , 'salary':salary})
   

def about(request):
    return render(request , 'about.html')

def thank(request):
    return render(request , 'thank.html')    


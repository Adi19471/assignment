from django.http.response import HttpResponse
from django.shortcuts import redirect, render



from.models import Assignments, Employe
from.forms import AssignmentsForm,EmployeForm,SignupForm

#  messages import
from django.contrib import messages
# user form
# from django.contrib.auth.forms import SignupForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth


import calendar
import time








def assignment_view(request):
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)

    l = ts,int(True)
    s = '-'.join(str(n) for n in l)
    initial_data = {'assign_id':s}
    # name_of_title = {'name_of_title'+{}}

    if request.method=="POST":
        fm = AssignmentsForm(request.POST,request.FILES,initial= initial_data)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your Data Has Sucessfulluy Saved check it...')
            return redirect('showdata')
           
    else:
        fm = AssignmentsForm(initial=initial_data)
    emp_detailes = Employe.objects.all()
    return render(request,'web/create-assignment.html',{"form":fm,'emp_detailes':emp_detailes})


# create employe form
def employe(request):
    if request.method=="POST":
        fm = EmployeForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.info(request, 'Your Data Has Sucessfulluy Saved check it...')
            return redirect('create-data')
            
    else:
        fm = EmployeForm()
    return render(request,'web/employecreate.html',{"form":fm})





# show assignment web page 

def allassignment_view(request):
        
    employe = Employe.objects.all()
    assignment_all = Assignments.objects.all()

    return render(request,'web/showassignment.html',{'assignment_all':assignment_all,'employe':employe})




# registraion form create it 

def registration_view(request):
    if request.method == "POST":
         fm = SignupForm(request.POST)
         if fm.is_valid():
             messages.success(request,'Account Created Succesfully...!')
             fm.save()
    else:
        fm = SignupForm()
    context = {"form":fm}
    return render(request,'web/registration.html',context)


# login page

def login_view(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'"Invalid Credienttial')
            return redirect('login')
    return render(request,'web/login.html')























# Create your views here.
def home_view(request):
    return render(request,'web/home.html')


def about_view(request):
    return render(request,'web/about.html')


def webportal_view(request):
    return render(request,'web/webportal.html')


def Task_view(request):
    return render(request,'web/Task.html')



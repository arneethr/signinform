from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

def homeview(request):
    return render(request,'resultsapp/home.html')

@login_required
def javaview(request):
    return render(request,'resultsapp/java.html')

@login_required
def pythonview(request):
    return render(request,'resultsapp/python.html')

@login_required
def aptitudeview(request):
    return render(request,'resultsapp/aptitude.html')

def logoutview(request):
    return render(request,'resultsapp/logout.html')

def signupview(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid:
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    form=SignupForm()
    return render(request,'resultsapp/signup.html',{'form':form})
from django.shortcuts import render
from django.http import HttpResponseRedirect
from testapp.forms import signup
# Create your views here.
from django.contrib.auth.decorators import login_required
def home_view(request):
    return(render(request,'testapp/home.html'))

@login_required
def java_view(request):
    return(render(request,'testapp/javaexam.html'))
def logoutview(request):
    return(render(request,'testapp/logout.html'))

def signupview(request):
    form=signup()
    if request.method=="POST":
        form=signup(request.POST)
        if form.is_valid():
          user=form.save()
          user.set_password(user.password)
          user.save()
          return HttpResponseRedirect('/accounts/login/')
    return(render(request,'testapp/signup.html',{'form':form}))

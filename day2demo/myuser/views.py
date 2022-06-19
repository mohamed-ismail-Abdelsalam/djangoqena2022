from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Myuser
from .forms import *
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin,logout
# Create your views here.
class Loginclass(View):
    def get(self,request):
        return render(request,'myuser/login.html')
    def post(self,request):
        print('in login class')
        loggeduser = Myuser.objects.filter(username=request.POST['exampleInputusername'],
                                           password=request.POST['exampleInputPassword'])
        authuser=authenticate(username=request.POST['exampleInputusername'],
                                           password=request.POST['exampleInputPassword'])
        print(authuser,'====')
        print(loggeduser[0].username,'---')
        if (len(loggeduser) != 0 and authuser is not None):
            authlogin(request,authuser)
            request.session['userid'] = loggeduser[0].id
            request.session['username'] = loggeduser[0].username
            print(request.session['username'])
            #return render(request, 'index.html')
            return HttpResponseRedirect('/admin/login/')
        else:
            return HttpResponseRedirect('/Login/')

def Login(request):
    if(request.method=='GET'):
        return render(request,'myuser/login.html')
    else:
       loggeduser= Myuser.objects.filter(username=request.POST['exampleInputusername'],password=request.POST['exampleInputPassword'])

       if(len(loggeduser)!=0):
           request.session['userid']=loggeduser[0].id
           request.session['username']=loggeduser[0].username
           print(request.session['username'])
           return render(request,'index.html')
def Register(request):

    f=RegsiterForm()
    context={}
    context['form']=f
    if(request.method=='GET'):
        return render(request,'myuser/register.html',context)
    else:
        f = RegsiterForm(request.POST)
        if(f.is_valid()):
            #insert myuser
            us=Myuser()
            us.username=request.POST['username']
            us.password=request.POST['password']
            us.email=request.POST['email']
            us.save()
            User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'],is_staff=True)

            #redirecg login view
            return HttpResponseRedirect('/Login')
        else:
            context['errors']=f.errors
            return render(request, 'myuser/register.html', context)
'''
def Register(request):
    f = RegsiterFormmodel()
    context = {}
    if(request.method=='GET'):
        context['form'] = f

        return render(request, 'myuser/register.html', context)
    else:
        f = RegsiterFormmodel(request.POST)
        if(f.is_valid()):
            f.save()
            return HttpResponseRedirect('/Login')
        else:
            context['errors'] = f.errors
            return render(request, 'myuser/register.html', context)
'''

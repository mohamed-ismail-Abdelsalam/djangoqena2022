from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Myuser
from .forms import *
# Create your views here.

def login(req):
    if('loginid' not in req.session):
        if(req.method=='GET'):
            return render(req,'myuser/login.html',{})
        else:
            user=Myuser.objects.filter(username=req.POST['username'],password=req.POST['exampleInputPassword'])
            print(len(user))
            if(len(user)!=0):
                req.session['loginid']=user[0].id
                return HttpResponseRedirect('/Trainee/Home')
                #return render(req, 'trainee/home.html', {})
            else:
                return render(req, 'myuser/login.html', {'error':'invalid credentails'})
    else:
        return HttpResponseRedirect('/Trainee/Home')
def register(req):
    context={}
    form=Register()
    if(req.method=='GET'):
        context['form']=form
        return render(req,'myuser/register.html',context)
    else:
        form=Register(req.POST)
        if(form.is_valid()):
            u=Myuser()
            u.email=req.POST['']
            u.username=req.POST['']
            u.password=req.POST['']
            u.save()
        return render(req, 'myuser/login.html', context)
def register2(req):
    context={}
    form=Register2()
    if(req.method=='GET'):
        context['form']=form
        return render(req,'myuser/register.html',context)
    else:
        form=Register2(req.POST)
        if(form.is_valid()):
            form.save()
        return render(req, 'myuser/login.html', context)
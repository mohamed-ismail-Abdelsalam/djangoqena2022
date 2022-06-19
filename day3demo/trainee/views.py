from django.shortcuts import render
from django.http import HttpResponse
from myuser.models import *
from .models import *
# Create your views here.
def Home(req):
    if('loginid' in req.session):
        '''
        c=Course(name='linux')
        c.save()
        t=Trainee()
        t.name='ismail'
        t.brnach=1
        t.courses=c
        t.save()
        '''
        loggeduser=Myuser.objects.get(id=req.session['loginid'])
        context={}
        context['username']=loggeduser.username
        context['trainees']=Trainee.objects.all()
        return render(req,'trainee/home.html',context)
    else:
        return render(req, 'myuser/login.html')


def Delete(req,id):
    return HttpResponse('deleted'+str(id))
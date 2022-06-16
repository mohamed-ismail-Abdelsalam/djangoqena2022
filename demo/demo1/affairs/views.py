from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def listsrudent(req):
    return HttpResponse('list student')
def insertstudent(req):
    return HttpResponse('inserted')


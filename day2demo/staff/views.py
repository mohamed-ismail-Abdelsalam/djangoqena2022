from django.shortcuts import render

# Create your views here.
def liststaff(request):
    return render(request,'staffindex.html')
def insert(r):
    return render(r,'staffinsert.html')

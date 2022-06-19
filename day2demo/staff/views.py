from django.shortcuts import render

# Create your views here.
def liststaff(request):
    request.session.clear()
    if('userid' in request.session):
        return render(request,'staffindex.html')
    else:
        return render(request, 'myuser/login.html')
def insert(r):
    return render(r,'staffinsert.html')

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
# Create your views here.
def liststaff(request):
    #print(request.META)
    '''
    if(request.get_host()=='localhost:9000'):
        return HttpResponse('Lists Staff')
    else:
        return HttpResponse('wrong host')

    if(request.is_secure()):
        print('secure')
        return HttpResponse('Lists Staff  secure')
    else:
        return HttpResponse('Lists Staff not secure')
    '''
    res=HttpResponse('Hr List')
    res.write('<h1>hi qena staff<h2>')
    res['content-type']='text/plain'
    res.set_cookie('name','sara')
    return res

def login(request):
    return HttpResponseRedirect('/HR/home')

def home(req):
    #return HttpResponse('rediredtd from login view')
    return JsonResponse({'name':'sara','id':1})
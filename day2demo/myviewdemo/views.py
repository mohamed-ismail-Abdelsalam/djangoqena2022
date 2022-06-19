from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods,require_GET,require_POST
from django.views import View
from  django.views.generic import ListView,CreateView
from trainee2.models import *
# Create your views here.
#@require_http_methods(["POST",'GET'])
#@require_POST()
def testgetdocrator(request):
    return render(request,'asd.html',{'method':request.method})

class Testgetdocratorclass(View):
    def get(self,request):
        print('get method in class')
        return render(request,'asd.html',{'method':request.method})
    def post(self,request):
        print('post method in class')
        return render(request,'asd.html',{'method':request.method})

class Listraineg(ListView):
    model = Trainee
class Inserttraineeg(CreateView):
    model=Trainee
    fileds='__all__'
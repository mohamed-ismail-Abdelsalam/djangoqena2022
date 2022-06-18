from django.shortcuts import render
from  django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import Trainee,Course
# Create your views here.
def listtrainee(req):
    trainees=Trainee.objects.all()
    for trainee in trainees:
        print(trainee.id,trainee.name,trainee.courses)
    #print(trainees,type(trainees))
    #return HttpResponse('liste')
    context={}
    context['title']='List page for qena trrainee'
    context['trainees']=trainees
    return render(req,'index.html',context)
def insert(r):
    '''
    c=Course(name='linux admin1')
    c.save()

    t=Trainee(name='rasmy',brnach=10)
    t.courses=Course.objects.get(id=1)
    t.save()
    '''
    context={}
    # get courses
    courses = Course.objects.all()
    context['courses'] = courses
    context['id']=1
    if(r.method=='GET'):
        #send it to insert.html
        return render(r,'insert.html',context)
    else:
            print(r.POST)
            Trainee.objects.create(name=r.POST['name'],courses=Course.objects.get(id=r.POST['course']),brnach=r.POST['Branch'])
            #return HttpResponse('inserted')
            return render(r,'insert.html',context)
def update(request):

    t=Trainee.objects.get(name='aya')

    if(t is not None):
        t.name='aya'
        t.save()
        return HttpResponse('updated')
    else:
        return  HttpResponse('not founde')
def delete(r):

    x=Trainee.objects.raw("delete from trainee2_trainee where name='rasmy'; ")
    print(x)
    '''
    c=Course(name='flask')
    print(c)
    print('ahmed',1,1.1,True,[1,3])
    '''
    return HttpResponse('deleted')
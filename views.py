from django.shortcuts import render,redirect
from todoapp.forms import todoform
from todoapp.models import todotable
def set(request):
    if request.method=="POST":
        info=todoform(request.POST)
        info.save()
        alltask=todotable.objects.all()
        t=todoform()
        data={'task':t,'alltask':alltask}
        return render(request,'index.html',data)
        #return redirect('/add')
    t=todoform()
    data={'task':t}
    return render(request,'index.html',data)

# def showalltask(request):
#     alltask=todotable.objects.all()
#     at={'alltask':alltask}
#     return render(request,'show.html',at)
    

def taskcancel(request,id):
        deltask=todotable.objects.get(id=id)
        deltask.delete()
        return redirect('/')

def taskclear(request):
        clrtask=todotable.objects.all()
        clrtask.delete()
        return redirect('/')


    



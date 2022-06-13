from multiprocessing import context
from django.shortcuts import redirect, render,get_object_or_404
from .models import *
from .forms import *
# from django.http import HttpResponse
# Create your views here.

def index(request):
    mainpost_list= Mainpost.objects.order_by('-created_date')
    print(1234)
    context={'mainpost_list':mainpost_list}
    return render(request,'board/mainpost_list.html',context)

def detail(request, mainpost_id):
    mainpost=get_object_or_404(Mainpost,pk=mainpost_id)
    context={'mainpost':mainpost}
    return render(request,'board/mainpost_detail.html',context)

def mainpost_create(request):
    if request.method =='POST':
        form=MainpostForm(request.POST)
        if form.is_valid():
            mainpost=form.save()
            return redirect('board:index')

    else:
        form=MainpostForm()
    return render(request,'board/mainpost_form.html',{'form':form})
from multiprocessing import context
from django.shortcuts import redirect, render,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# from django.http import HttpResponse
# Create your views here.

# def index(request): #글 목록페이지
#     mainpost_list= Mainpost.objects.order_by('-created_date')

#     context={'mainpost_list':mainpost_list}
#     return render(request,'board/mainpost_list.html',context)

def index(request): #글 목록페이지
    page=request.GET.get('page','1')
    mainpost_list= Mainpost.objects.order_by('-created_date')
    paginator=Paginator(mainpost_list,10)

    page_obj=paginator.get_page(page)

    context={'mainpost_list':page_obj, 'page':page}
    return render(request,'board/mainpost_list.html',context)

def detail(request, mainpost_id): #글 상세페이지
    mainpost=get_object_or_404(Mainpost,pk=mainpost_id)
    context={'mainpost':mainpost}
    return render(request,'board/mainpost_detail.html',context)

@login_required(login_url='common:login')
def mainpost_create(request):  #글쓰기
    if request.method =='POST':
        form=MainpostForm(request.POST)
        if form.is_valid():
            mainpost=form.save(commit=False)
            mainpost.author=request.user
            mainpost.save()
            return redirect('board:index')

    else:
        form=MainpostForm()
    return render(request,'board/mainpost_form.html',{'form':form})

@login_required(login_url='common:login')
def comment_create(request,mainpost_id):
    if request.method=='POST':
        mainpost=get_object_or_404(Mainpost,pk=mainpost_id)
        mainpost.comment_set.create(text=request.POST.get('text'),created_date=timezone.now(),author=request.user)
        return redirect('board:detail',mainpost_id=mainpost.id)



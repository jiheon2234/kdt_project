from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from common.forms import UserForm

# Create your views here.

def mainpage(request):
    return render(request,'common/index.html')

def mypage(request):

    return render(request,'common/mypage.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            # login(request, user)  # 로그인
            return redirect('common:login')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def id_check(request):
    try:
        user=User.objects.get(username=request.GET['username'])
       
    except:
        user=None
    result={
        'result':'success',
        'data': 'exist' if user else 'not exist'
    }
    
    return JsonResponse(result)
    
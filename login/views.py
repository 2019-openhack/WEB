from django.shortcuts import render
from .models import User
from django.contrib import auth
from django.http import *

# Create your views here.
def login(request):
    return render(request, "login/login.html", {})

def main(request):
    return render(request, "login/main.html", {})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def index(request):
    #로그인이 잘 되어있나 확인하기 위해 user name 길이 체크
    if (len(request.user.username) > 0):
        print(User.objects.values('name'))
        checklist = list(User.objects.values('name'))
        
        try:
            # check if the account is already created or not.
            for element in checklist:
                if element['name'] == request.user.username:
                    # 이미 생성된 계정임.
                    print("it is detected")

            # 새로운 유저 생성
        except:
            new_user = User.objects.create(
                name=request.user.username,
                email=request.user.email
            )
            print("new user")
            # 새로운 유저 만들었을 때
            return render(request, 'home/index.html', {'newbie': True})
        #로그인 된 상태에서 index 리턴
        return render(request, 'home/main.html', {'newbie':False})
    #로그아웃 된 상태에서 index 리턴
    return render(request, 'home/index.html', {'newbie':False})


from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import connection
from .models import UserProfile
def index(request):
    return render(request,
                  "DemoApp/index.html",
                  )


def profile(request):
    return render(request,
                  "DemoApp/profile.html",
                  )


def login(request):
    if request.method == 'GET':
        context = ''
        return render(request, 'DemoApp/login.html', {'context': context})

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print(username,password)
        cursor = connection.cursor()
        user = None
        sql = "SELECT balance FROM demoapp_userprofile WHERE username= '"+username+"' AND password = '"+password+"'"
        print(sql)
        with connection.cursor() as cursor:
            cursor.execute(sql)
            balance = cursor.fetchone()[0]

        if balance is not None:
            context = {'username':username,'balance':balance}
            return render(request,
                          "DemoApp/profile.html",
                          context
                          )
        else:
            messages.error(request, f'Wrong username/password!')

            return render(request, 'DemoApp/login.html' )

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            balance = form.cleaned_data.get('balance')
            user = UserProfile(username = username , password = password, balance = balance)
            user.save()
            #form.save()
            messages.success(request, f'Welcome! Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'DemoApp/signup.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('/login/')


def login_view(request):
    return render(request, 'login/login.html')
from django.shortcuts import render

def login_view(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')

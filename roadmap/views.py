from django.shortcuts import render


def about_us(request):
    return render(request, 'about.html')

def join_us(request):
    return render(request, 'join.html')

def help_center(request):
    return render(request, 'help_center.html')

def terms(request):
    return render(request, 'terms.html')

def privacy(request):
    return render(request, 'privacy.html')
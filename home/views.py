from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def blog(request):
    return render(request, 'home/blog.html')

def contact(request):
    return render(request, 'home/contact.html')

def faq(request):
    return render(request, 'home/faq.html')

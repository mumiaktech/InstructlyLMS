from django.shortcuts import render

def courses(request):
    return render(request, 'materials/courses.html')
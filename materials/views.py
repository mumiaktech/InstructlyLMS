from django.shortcuts import render, get_object_or_404
from .models import Course, Category

def courses(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category', None)

    if selected_category:
        courses = Course.objects.filter(category__id=selected_category)
    else:
        courses = Course.objects.all()

    return render(request, 'materials/courses.html', {'courses': courses, 'categories': categories})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'materials/course-details.html', {'course': course})

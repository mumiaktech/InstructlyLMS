from django.urls import path
from . import views

urlpatterns = [
    #instructor urls
    path('create/', views.create_quiz, name='create_quiz'),
    path('instructor-list/', views.instructor_quiz_list, name='instructor_quiz_list'),  # For instructors
    path('quiz/<int:quiz_id>/add-questions/', views.add_questions, name='add_questions'),
    path('quiz/<int:quiz_id>/questions/', views.quiz_questions, name='quiz_questions'),
    
    #student urls
    path('take/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
    path('list/', views.quiz_list, name='quiz_list'),  # For students
    path('result/<int:attempt_id>/', views.quiz_result, name='quiz_result'),
]

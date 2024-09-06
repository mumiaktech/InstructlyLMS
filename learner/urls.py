from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_home, name='student'),

    path('resources/', views.student_resources, name='student_resources'),

    path('news/', views.news_view, name="news"),

    path('books/', views.search_books_view, name='search_books'),

    path('videos/', views.search_videos_view, name='search_videos'),
]

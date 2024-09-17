from django.urls import path
from . import views

urlpatterns = [
    #home url
    path('', views.student_home, name='student'),

    #resources url
    path('resources/', views.student_resources, name='student_resources'),

    #news url
    path('news/', views.news_view, name="news"),

    #books url
    path('books/', views.books_view, name='search_books'),

    #videos url
    path('videos/', views.videos_view, name='search_videos'),
]

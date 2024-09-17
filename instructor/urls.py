
from django.urls import path
from . import views

urlpatterns = [
    #dashboard url
    path('', views.instructor_dashboard, name='instructor'),

    #resources urls
    path('resources/', views.resource_list, name='resource_list'),
    path('resources_shared/', views.shared_resources, name='resource_shared'),
    path('resources/create/', views.resource_create, name='resource_create'),
    path('resources/<int:pk>/edit/', views.resource_edit, name='resource_edit'),
    path('resources/<int:pk>/delete/', views.resource_delete, name='resource_delete'),

    #settings, password and support urls
    path('user_settings/', views.user_settings, name='user_settings'),
    path('settings/', views.user_profile, name='settings'),
    path('create_user_profile/', views.create_user_profile, name='create_user_profile'),
    path('reset_password/', views.reset_password, name='reset_password'),  
    path('support/', views.instructor_support, name='help_support'),

    #activities and notifications urls
    path('recent-activity/', views.recent_activity, name='recent_activity'),
    path('notifications/', views.notifications, name='notifications'),

]

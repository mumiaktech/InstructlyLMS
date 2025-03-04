from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
    path('contact/success/', views.contact_success, name='contact_success'),
    path("faq/", views.faq, name="faq"),

    #Footer
    path("help/", views.help, name="help"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
]

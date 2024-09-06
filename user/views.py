from django.contrib.auth import authenticate, login
from django.contrib import messages
from rest_framework import generics
from .forms import CustomUserProfile
from .serializers import UserSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.conf import settings


#Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserProfile(request.POST)
        if form.is_valid():
            user = form.save()

            # Get the role from the form data
            role = request.POST.get('role')

            # Assign the user to the appropriate group based on the role
            if role == 'Instructor':
                instructor_group = Group.objects.get(name='Instructor')
                instructor_group.user_set.add(user)
            elif role == 'Student':
                student_group = Group.objects.get(name='Student')
                student_group.user_set.add(user)

            # Log the user in
            login(request, user)

            # Send confirmation email
            send_mail(
                'Registration Confirmation',
                'Thank you for registering with Instructly!.',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            # Display popup message
            messages.success(request, 'Registration successful! Please check your email for notification.')

            # Redirect the user to the same registration page or another relevant page
            return redirect('register')
    else:
        form = CustomUserProfile()
    return render(request, 'registration/register.html', {'form': form})

#Rgistration API
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

#Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Check the user’s group and redirect to the appropriate dashboard
            if user.groups.filter(name='Instructor').exists():
                return redirect('instructor')
            elif user.groups.filter(name='Student').exists():
                return redirect('student')
            else:
                return redirect('login') 
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'registration/index.html')

#Logout View
@login_required
def logout_page(request):
    if request.user.groups.filter(name='Instructor').exists():
        cancel_url = 'instructor'
    elif request.user.groups.filter(name='Student').exists():
        cancel_url = 'student'
    else:
        cancel_url = 'login' 

    context = {
        'cancel_url': cancel_url
    }
    return render(request, 'registration/logout.html', context)
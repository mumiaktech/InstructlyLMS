from django.contrib import messages
from .forms import ResourceForm, UserUpdateForm, UserProfileForm, PasswordResetForm, ReportForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Resource, UserProfile, Activity, Notification
from django.db.models import Q
from django.contrib.auth import update_session_auth_hash


#instructor dashboard
@login_required
def instructor_dashboard(request):
    # Count unread notifications
    notifications_count = Notification.objects.filter(user=request.user, is_read=False).count()
    
    return render(request, 'instructor/instructor_dashboard.html', {
        'notifications_count': notifications_count,
    })

#resources views
@login_required
def resource_list(request):
    query = request.GET.get('q', '')
    resources = Resource.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )
    return render(request, 'instructor/resource_list.html', {'resources': resources})

@login_required
def shared_resources(request):
    # Fetch resources for the logged-in user
    resources = Resource.objects.filter(owner=request.user)
    
    # Get the search query if it exists
    query = request.GET.get('q')
    if query:
        resources = resources.filter(title__icontains=query)
    
    return render(request, 'instructor/instructor_shared_resources.html', {
        'resources': resources,
    })

@login_required
def resource_create(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.created_by = request.user
            resource.owner = request.user
            resource.save()
            return redirect('resource_list')
    else:
        form = ResourceForm()
    return render(request, 'instructor/resource_form.html', {'form': form})

@login_required
def resource_edit(request, pk):
    resource = get_object_or_404(Resource, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
    else:
        form = ResourceForm(instance=resource)
    return render(request, 'instructor/resource_form.html', {'form': form})

@login_required
def resource_delete(request, pk):
    # Fetch the resource ensuring that the logged-in user is the owner
    resource = get_object_or_404(Resource, pk=pk, owner=request.user)
    
    if request.method == 'POST':
        resource.delete()
        return redirect('resource_list')
    
    return render(request, 'instructor/resource_confirm_delete.html', {'resource': resource})

#user settings view
@login_required
def user_settings(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Redirect to a page where the user can create a UserProfile
        return redirect('create_user_profile')  # Define this view if it doesn't exist

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('settings')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'instructor/user_settings.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def user_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Optionally, handle the case where UserProfile does not exist
        user_profile = None 

    return render(request, 'instructor/settings.html', {
        'user': request.user,
        'profile': user_profile
    })

@login_required
def create_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('settings')
    else:
        form = UserProfileForm()

    return render(request, 'instructor/create_user_profile.html', {
        'form': form
    })

#password view
@login_required
def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  
            return redirect('instructor')  
    else:
        form = PasswordResetForm(user=request.user)
    
    return render(request, 'instructor/reset_password.html', {'form': form})

#support view
def instructor_support(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your report has been submitted successfully.')
            return redirect('help_support')
    else:
        form = ReportForm()
    
    return render(request, 'instructor/help_support.html', {'form': form})

#activity view
@login_required
def recent_activity(request):
    # Fetch recent activities for the logged-in user
    activities = Activity.objects.filter(user=request.user).order_by('-date')[:5]
    return render(request, 'instructor/recent_activity.html', {'activities': activities})

#notification view
@login_required
def notifications(request):
    user_notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    user_notifications.update(is_read=True)
    return render(request, 'instructor/notifications.html', {'notifications': user_notifications})

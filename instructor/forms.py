from django import forms
from django.contrib.auth.models import User
from .models import Resource, UserProfile, Report
from django.contrib.auth.forms import PasswordChangeForm

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'resource_type', 'cost_type', 'description', 'url', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'resource_type': forms.Select(attrs={'class': 'form-select'}),
            'cost_type': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']  

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

class PasswordResetForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')
        widgets = {
            'old_password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter old password'
            }),
            'new_password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter new password'
            }),
            'new_password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm new password'
            }),
        }

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name', 'email', 'subject', 'description', 'screenshot', 'priority']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'screenshot': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
        }

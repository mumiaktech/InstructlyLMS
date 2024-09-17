from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#custome user profile form
class CustomUserProfile(UserCreationForm):
    role = forms.ChoiceField(choices=[('Admin', 'Admin'), ('Instructor', 'Instructor'), ('Student', 'Student')])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['role'].widget.attrs.update({'class': 'form-select'})
from django import forms
from .models import Quiz, Question, Answer

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description', 'time_limit']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter quiz title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter quiz description'}),
            'time_limit': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter time limit in minutes'}),
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter question text'}),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'is_correct']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter answer text'}),
            'is_correct': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

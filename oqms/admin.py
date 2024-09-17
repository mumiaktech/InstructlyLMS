from django.contrib import admin
from .models import Question, Quiz, QuizAttempt, Answer, StudentAnswer

# Register your models here.
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(QuizAttempt)
admin.site.register(Answer)
admin.site.register(StudentAnswer)
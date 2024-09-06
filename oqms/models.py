from django.db import models
from django.contrib.auth.models import User

# Quiz model representing a quiz created by an instructor
class Quiz(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    time_limit = models.IntegerField(help_text="Time limit in minutes")
    
    def __str__(self):
        # String representation of the quiz, showing its title
        return self.title

# Question model representing a question in a quiz
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    
    def __str__(self):
        # String representation of the question, showing its text
        return self.text

# Answer model representing an answer to a specific question
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        # String representation of the answer, showing its text
        return self.text

# QuizAttempt model representing a student's attempt at a quiz
class QuizAttempt(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_attempts')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField()
    completed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        # String representation of the quiz attempt, showing the student's username and quiz title
        return f'{self.student.username} - {self.quiz.title}'

# StudentAnswer model representing the student's selected answer in a quiz attempt
class StudentAnswer(models.Model):
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name='student_answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    
    def __str__(self):
        # String representation of the student's answer, showing the student's username and question text
        return f'{self.attempt.student.username} - {self.question.text}'

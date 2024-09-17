from django.test import TestCase
from django.contrib.auth.models import User
from .models import Quiz, Question, Answer, QuizAttempt, StudentAnswer
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Unit tests
class QuizModelTest(TestCase):
    def setUp(self):
        # Set up a user (instructor) and a quiz for testing
        self.instructor = User.objects.create_user(username='instructor', password='12345')
        self.quiz = Quiz.objects.create(
            instructor=self.instructor,
            title='Sample Quiz',
            description='This is a sample quiz.',
            time_limit=30
        )

    def test_quiz_creation(self):
        # Test if the quiz is created with correct attributes
        self.assertEqual(self.quiz.title, 'Sample Quiz')
        self.assertEqual(self.quiz.instructor.username, 'instructor')
        self.assertEqual(self.quiz.time_limit, 30)

    def test_quiz_str(self):
        # Test the string representation of the Quiz model
        self.assertEqual(str(self.quiz), 'Sample Quiz')


class QuestionModelTest(TestCase):
    def setUp(self):
        # Set up a quiz and a question for testing
        self.instructor = User.objects.create_user(username='instructor', password='12345')
        self.quiz = Quiz.objects.create(
            instructor=self.instructor,
            title='Sample Quiz',
            description='This is a sample quiz.',
            time_limit=30
        )
        self.question = Question.objects.create(quiz=self.quiz, text='What is Django?')

    def test_question_creation(self):
        # Test if the question is created with the correct text
        self.assertEqual(self.question.text, 'What is Django?')
        self.assertEqual(self.question.quiz.title, 'Sample Quiz')

    def test_question_str(self):
        # Test the string representation of the Question model
        self.assertEqual(str(self.question), 'What is Django?')


class AnswerModelTest(TestCase):
    def setUp(self):
        # Set up a quiz, a question, and an answer for testing
        self.instructor = User.objects.create_user(username='instructor', password='12345')
        self.quiz = Quiz.objects.create(
            instructor=self.instructor,
            title='Sample Quiz',
            description='This is a sample quiz.',
            time_limit=30
        )
        self.question = Question.objects.create(quiz=self.quiz, text='What is Django?')
        self.answer = Answer.objects.create(question=self.question, text='A web framework', is_correct=True)

    def test_answer_creation(self):
        # Test if the answer is created with correct text and correctness flag
        self.assertEqual(self.answer.text, 'A web framework')
        self.assertTrue(self.answer.is_correct)

    def test_answer_str(self):
        # Test the string representation of the Answer model
        self.assertEqual(str(self.answer), 'A web framework')


class QuizAttemptModelTest(TestCase):
    def setUp(self):
        # Set up an instructor, student, quiz, and quiz attempt for testing
        self.instructor = User.objects.create_user(username='instructor', password='12345')
        self.student = User.objects.create_user(username='student', password='12345')
        self.quiz = Quiz.objects.create(
            instructor=self.instructor,
            title='Sample Quiz',
            description='This is a sample quiz.',
            time_limit=30
        )
        self.attempt = QuizAttempt.objects.create(student=self.student, quiz=self.quiz, score=85.0)

    def test_quiz_attempt_creation(self):
        # Test if the quiz attempt is created with the correct score and student
        self.assertEqual(self.attempt.student.username, 'student')
        self.assertEqual(self.attempt.quiz.title, 'Sample Quiz')
        self.assertEqual(self.attempt.score, 85.0)

    def test_quiz_attempt_str(self):
        # Test the string representation of the QuizAttempt model
        self.assertEqual(str(self.attempt), 'student - Sample Quiz')


class StudentAnswerModelTest(TestCase):
    def setUp(self):
        # Set up all the required data for a student's quiz attempt and answers
        self.instructor = User.objects.create_user(username='instructor', password='12345')
        self.student = User.objects.create_user(username='student', password='12345')
        self.quiz = Quiz.objects.create(
            instructor=self.instructor,
            title='Sample Quiz',
            description='This is a sample quiz.',
            time_limit=30
        )
        self.question = Question.objects.create(quiz=self.quiz, text='What is Django?')
        self.answer = Answer.objects.create(question=self.question, text='A web framework', is_correct=True)
        self.attempt = QuizAttempt.objects.create(student=self.student, quiz=self.quiz, score=85.0)
        self.student_answer = StudentAnswer.objects.create(
            attempt=self.attempt,
            question=self.question,
            selected_answer=self.answer
        )

    def test_student_answer_creation(self):
        # Test if the student's selected answer is correctly stored
        self.assertEqual(self.student_answer.attempt.student.username, 'student')
        self.assertEqual(self.student_answer.question.text, 'What is Django?')
        self.assertEqual(self.student_answer.selected_answer.text, 'A web framework')

    def test_student_answer_str(self):
        # Test the string representation of the StudentAnswer model
        self.assertEqual(str(self.student_answer), 'student - What is Django?')


# Integration tests
class QuizIntegrationTest(TestCase):
    def setUp(self):
        # Set up data for integration tests, including users, quiz, questions, and answers
        self.instructor = User.objects.create_user(username='instructor', password='12345')
        self.student = User.objects.create_user(username='student', password='12345')
        
        # Create a quiz
        self.quiz = Quiz.objects.create(
            instructor=self.instructor,
            title='Django Basics Quiz',
            description='A quiz on Django basics.',
            time_limit=30
        )
        
        # Create questions and answers for the quiz
        self.question1 = Question.objects.create(quiz=self.quiz, text='What is Django?')
        self.question2 = Question.objects.create(quiz=self.quiz, text='What is a Model?')
        self.answer1 = Answer.objects.create(question=self.question1, text='A web framework', is_correct=True)
        self.answer2 = Answer.objects.create(question=self.question1, text='A database', is_correct=False)
        self.answer3 = Answer.objects.create(question=self.question2, text='A database table', is_correct=True)
        self.answer4 = Answer.objects.create(question=self.question2, text='A web framework', is_correct=False)
        
        # Simulate a quiz attempt
        self.attempt = QuizAttempt.objects.create(student=self.student, quiz=self.quiz, score=0.0)

    def test_quiz_workflow(self):
        # Test the entire workflow of a student taking the quiz
        self.assertEqual(self.quiz.title, 'Django Basics Quiz')
        self.assertEqual(self.quiz.instructor.username, 'instructor')
        self.assertEqual(self.question1.quiz, self.quiz)
        
        # Simulate answering questions
        StudentAnswer.objects.create(attempt=self.attempt, question=self.question1, selected_answer=self.answer1)
        StudentAnswer.objects.create(attempt=self.attempt, question=self.question2, selected_answer=self.answer3)
        
        # Calculate the score based on correct answers
        correct_answers = 0
        for student_answer in self.attempt.student_answers.all():
            if student_answer.selected_answer.is_correct:
                correct_answers += 1
        
        # Update score based on correct answers
        self.attempt.score = (correct_answers / 2) * 100
        self.attempt.save()

        # Check if the score is correct and the workflow completes
        self.assertEqual(self.attempt.score, 100.0)
        self.assertEqual(self.attempt.student_answers.count(), 2)


# End-to-end tests using Selenium
    def test_instructor_creates_quiz(self):
        # Open browser and go to login page to simulate instructor login
        self.browser.get(f'{self.live_server_url}/login/')
        
        # Enter login credentials
        username_input = self.browser.find_element(By.NAME, "username")
        username_input.send_keys('instructor')
        password_input = self.browser.find_element(By.NAME, "password")
        password_input.send_keys('12345')
        password_input.send_keys(Keys.RETURN)
        
        # Ensure login is successful by checking for the dashboard
        time.sleep(2)
        self.assertIn("Dashboard", self.browser.page_source)
        
        # Go to quiz creation page
        self.browser.get(f'{self.live_server_url}/quiz/create/')
        
        # Fill in quiz details and submit
        title_input = self.browser.find_element(By.NAME, "title")
        title_input.send_keys("Django Basics Quiz")
        description_input = self.browser.find_element(By.NAME, "description")
        description_input.send_keys("A test quiz for Django basics.")
        time_limit_input = self.browser.find_element(By.NAME, "time_limit")
        time_limit_input.send_keys("30")
        time_limit_input.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
        # Check if the quiz was created successfully
        self.assertIn("Quiz created successfully", self.browser.page_source)

    def test_instructor_adds_questions_to_quiz(self):
        # Simulate quiz creation and adding questions as an instructor
        self.test_instructor_creates_quiz()
        
        # Go to question creation page for the quiz
        self.browser.get(f'{self.live_server_url}/quiz/1/add_questions/')  # assuming quiz ID is 1
        
        # Fill in question details
        question_input = self.browser.find_element(By.NAME, "question_text")
        question_input.send_keys("What is Django?")
        answer_input = self.browser.find_element(By.NAME, "answer_text")
        answer_input.send_keys("A web framework")
        
        # Submit the question
        answer_input.send_keys(Keys.RETURN)
        time.sleep(2)
        
        # Ensure the question was added successfully
        self.assertIn("Question added successfully", self.browser.page_source)

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Quiz, Question, Answer, QuizAttempt, StudentAnswer
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#unit tests
class QuizModelTest(TestCase):
    def setUp(self):
        self.instructor = User.objects.create_user(username='instructor', password='12345')
        self.quiz = Quiz.objects.create(
            instructor=self.instructor,
            title='Sample Quiz',
            description='This is a sample quiz.',
            time_limit=30
        )

    def test_quiz_creation(self):
        self.assertEqual(self.quiz.title, 'Sample Quiz')
        self.assertEqual(self.quiz.instructor.username, 'instructor')
        self.assertEqual(self.quiz.time_limit, 30)

    def test_quiz_str(self):
        self.assertEqual(str(self.quiz), 'Sample Quiz')


class QuestionModelTest(TestCase):
    def setUp(self):
        self.instructor = User.objects.create_user(username='instructor', password='12345')
        self.quiz = Quiz.objects.create(
            instructor=self.instructor,
            title='Sample Quiz',
            description='This is a sample quiz.',
            time_limit=30
        )
        self.question = Question.objects.create(quiz=self.quiz, text='What is Django?')

    def test_question_creation(self):
        self.assertEqual(self.question.text, 'What is Django?')
        self.assertEqual(self.question.quiz.title, 'Sample Quiz')

    def test_question_str(self):
        self.assertEqual(str(self.question), 'What is Django?')


class AnswerModelTest(TestCase):
    def setUp(self):
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
        self.assertEqual(self.answer.text, 'A web framework')
        self.assertTrue(self.answer.is_correct)

    def test_answer_str(self):
        self.assertEqual(str(self.answer), 'A web framework')


class QuizAttemptModelTest(TestCase):
    def setUp(self):
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
        self.assertEqual(self.attempt.student.username, 'student')
        self.assertEqual(self.attempt.quiz.title, 'Sample Quiz')
        self.assertEqual(self.attempt.score, 85.0)

    def test_quiz_attempt_str(self):
        self.assertEqual(str(self.attempt), 'student - Sample Quiz')


class StudentAnswerModelTest(TestCase):
    def setUp(self):
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
        self.assertEqual(self.student_answer.attempt.student.username, 'student')
        self.assertEqual(self.student_answer.question.text, 'What is Django?')
        self.assertEqual(self.student_answer.selected_answer.text, 'A web framework')

    def test_student_answer_str(self):
        self.assertEqual(str(self.student_answer), 'student - What is Django?')



#Integration tests
class QuizIntegrationTest(TestCase):
    def setUp(self):
        # Create users
        self.instructor = User.objects.create_user(username='instructor', password='12345')
        self.student = User.objects.create_user(username='student', password='12345')
        
        # Create a quiz
        self.quiz = Quiz.objects.create(
            instructor=self.instructor,
            title='Django Basics Quiz',
            description='A quiz on Django basics.',
            time_limit=30
        )
        
        # Create questions for the quiz
        self.question1 = Question.objects.create(quiz=self.quiz, text='What is Django?')
        self.question2 = Question.objects.create(quiz=self.quiz, text='What is a Model?')
        
        # Create answers for the questions
        self.answer1 = Answer.objects.create(question=self.question1, text='A web framework', is_correct=True)
        self.answer2 = Answer.objects.create(question=self.question1, text='A database', is_correct=False)
        self.answer3 = Answer.objects.create(question=self.question2, text='A database table', is_correct=True)
        self.answer4 = Answer.objects.create(question=self.question2, text='A web framework', is_correct=False)
        
        # Simulate a quiz attempt
        self.attempt = QuizAttempt.objects.create(student=self.student, quiz=self.quiz, score=0.0)

    def test_quiz_workflow(self):
        # Check if the quiz was created correctly
        self.assertEqual(self.quiz.title, 'Django Basics Quiz')
        self.assertEqual(self.quiz.instructor.username, 'instructor')

        # Check if the questions are associated with the quiz
        self.assertEqual(self.question1.quiz, self.quiz)
        self.assertEqual(self.question2.quiz, self.quiz)
        self.assertEqual(self.question1.text, 'What is Django?')

        # Check if answers are associated with the questions
        self.assertEqual(self.answer1.question, self.question1)
        self.assertEqual(self.answer2.question, self.question1)
        self.assertTrue(self.answer1.is_correct)
        self.assertFalse(self.answer2.is_correct)

        # Simulate answering the questions correctly and submitting the quiz attempt
        StudentAnswer.objects.create(
            attempt=self.attempt,
            question=self.question1,
            selected_answer=self.answer1
        )
        StudentAnswer.objects.create(
            attempt=self.attempt,
            question=self.question2,
            selected_answer=self.answer3
        )

        # Update the score based on correct answers
        correct_answers = 0
        for student_answer in self.attempt.student_answers.all():
            if student_answer.selected_answer.is_correct:
                correct_answers += 1

        # Assume each question is worth 50 points, calculate the score
        self.attempt.score = (correct_answers / 2) * 100
        self.attempt.save()

        # Check if the score is calculated correctly
        self.assertEqual(self.attempt.score, 100.0)

        # Ensure that the attempt and student answers are related correctly
        self.assertEqual(self.attempt.student.username, 'student')
        self.assertEqual(self.attempt.quiz, self.quiz)
        self.assertEqual(self.attempt.student_answers.count(), 2)

#end to end tests using selenium
    def test_instructor_creates_quiz(self):
        # Open the browser and go to the login page
        self.browser.get(f'{self.live_server_url}/login/')
        
        # Enter login credentials
        username_input = self.browser.find_element(By.NAME, "username")
        username_input.send_keys('instructor')
        password_input = self.browser.find_element(By.NAME, "password")
        password_input.send_keys('12345')
        password_input.send_keys(Keys.RETURN)
        
        # Ensure we are logged in by checking for a dashboard link
        time.sleep(2)
        self.assertIn("Dashboard", self.browser.page_source)
        
        # Go to quiz creation page
        self.browser.get(f'{self.live_server_url}/quiz/create/')
        
        # Fill out the form for quiz creation
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
        # First login as the instructor
        self.test_instructor_creates_quiz()
        
        # Go to the quiz question creation page
        self.browser.get(f'{self.live_server_url}/quiz/1/add_questions/')  # assuming the quiz ID is 1
        
        # Add a question
        question_input = self.browser.find_element(By.NAME, "text")
        question_input.send_keys("What is Django?")
        question_input.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
        # Add answers to the question
        answer_input1 = self.browser.find_element(By.NAME, "answer_1")
        answer_input1.send_keys("A web framework")
        self.browser.find_element(By.NAME, "correct_1").click()  # Mark as correct answer
        
        answer_input2 = self.browser.find_element(By.NAME, "answer_2")
        answer_input2.send_keys("A programming language")
        answer_input2.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
        # Check if the questions and answers were added successfully
        self.assertIn("Question added successfully", self.browser.page_source)

    def test_student_attempts_quiz(self):
        # Open the browser and go to the login page
        self.browser.get(f'{self.live_server_url}/login/')
        
        # Enter login credentials for student
        username_input = self.browser.find_element(By.NAME, "username")
        username_input.send_keys('student')
        password_input = self.browser.find_element(By.NAME, "password")
        password_input.send_keys('12345')
        password_input.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
        # Go to the quiz page
        self.browser.get(f'{self.live_server_url}/quiz/1/take/')  # assuming quiz ID 1
        
        # Answer the first question
        answer_choice = self.browser.find_element(By.XPATH, "//input[@name='answer' and @value='A web framework']")
        answer_choice.click()
        self.browser.find_element(By.ID, "submit_answer").click()
        
        time.sleep(2)
        
        # Submit the quiz
        self.browser.find_element(By.ID, "submit_quiz").click()
        
        time.sleep(2)
        
        # Check if the quiz was submitted successfully and score is shown
        self.assertIn("Quiz submitted successfully", self.browser.page_source)
        self.assertIn("Your score is", self.browser.page_source)

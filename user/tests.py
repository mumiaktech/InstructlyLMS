from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class QuizEndToEndTest(LiveServerTestCase):
    def setUp(self):
        # Setup the WebDriver (Chrome in this case, use Geckodriver for Firefox)
        self.browser = webdriver.Chrome()
        # Create test users
        self.instructor = User.objects.create_user(username='instructor', password='12345')
        self.student = User.objects.create_user(username='student', password='12345')

    def tearDown(self):
        # Close the browser after each test
        self.browser.quit()

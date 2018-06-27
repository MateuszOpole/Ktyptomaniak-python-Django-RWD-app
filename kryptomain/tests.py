from django.test import TestCase

import datetime

from django.utils import timezone
from django.test import Client
from django.test.utils import setup_test_environment
from django.urls import reverse
from django.test.client import Client
from .models import *
from .forms import *   
# Create your tests here.
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_post(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = TematycznyPost(data_wpisu=time)
        self.assertIs(future_post.was_published_recently(), False)
		
class ViewmodelTests(TestCase):
	def test_index(self):
        # Issue a GET request.
		client = Client()
		response=client.get(reverse('index'))
		response.status_code
		response.content
		
	def test_login(self):	
		client = Client()
		response=client.post(reverse('login'), {'username': 'mati', 'password': 'zetor1994'})
		response.content
		response.status_code
		
	
class Setup_Class(TestCase):

	def setUp(self):
		self.user = User.objects.create(username="test", first_name="user",last_name="user2",email="user@mp.com", password1="userpas", password2="userpas")
		
class User_Form_Test(TestCase):

    # Valid Form Data
	def test_UserForm_valid(self):
		form = RejestracjaForm(data={'username':"test" ,'first_name': "user",'last_name':"user2",'email': "user@mp.com",'password1': "userpas",'password2': "userpas"})
		self.assertTrue(form.is_valid())
	def test_UserForm_invalid(self):
		form = RejestracjaForm(data={'emaial': "", })
		self.assertFalse(form.is_valid())
	def test_KategoriaForm(self):
		form=KategoriaForm(data={'nazwa_kategorii':"test"})
		self.assertFalse(form.is_valid())
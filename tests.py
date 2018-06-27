from django.test import TestCase
import unittest
from django.test.client import Client

# Create your tests here.
def setUp(self):
        # Every test needs a client.
	response = c.get('/logowanie/')
	response.content
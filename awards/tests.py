from django.test import TestCase
from .models import *
# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        '''
        Method to be run in every beginning of the test
        '''
        self.photo = Profile('photo')

    def  test_instance(self):
        self.assertTrue(isinstance(self.photo,Profile))  


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

    # def test_save_method(self):
    #     '''
    #     Method to save profile
        
    #     '''
    #     self.photo.save_user()
    #     profile = Profile.objects.all()
    #     self.assertTrue(len(profile)>0)

# class Image(TestCase):
#     def setUp(self):

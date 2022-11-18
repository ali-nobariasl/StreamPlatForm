from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

# name of functions must start with test

class RegisterTestCase(APITestCase):
    
    def test_register(self):
        data = {
            "username": "testcase",
            "password": "testcase@123",
            "password2" :"testcase@123",
            "email": "testcase@g.com",
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

class LoginLogoutTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example",
                                             password="newpassword@123456")
        
    def test_login(self):
        data = {
            "username": "example",
            "password":"newpassword@123456"
        }
        response = self.client.post(reverse('login'),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_logout(self):
        self.token = Token.objects.get(user__username = "example")
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from watchlist_app.api import serializers
from watchlist_app import models


class StreamPlarformTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="example@123example")
        self.token = Token.objects.get(user__username = "example")
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)
        self.stream = models.StreamPlatform.objects.create(
                                                        name="Netflix",about="#1 Streaming Platform",
                                                        website= "http://netflix.com")
        
    def test_streamplarform_create(self):
        data = {
            "name":"Netflix",
            "about": "#1 Streaming Platform",
            "website": "http://netflix.com"
        }
        response = self.client.post(reverse('Platform-Viewset-list'), data)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)
        
    def test_streamplarform_list(self):
        response = self.client.get(reverse('Platform-Viewset-list'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_streamplarform_ind(self):
        response = self.client.get(reverse('Platform-Viewset-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    
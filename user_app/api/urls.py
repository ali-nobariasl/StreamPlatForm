from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import registerstion_view 


urlpatterns = [
    path('login/', obtain_auth_token, name ='login'),
    path('register/', registerstion_view, name ='register'),
    
]

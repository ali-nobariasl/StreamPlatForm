from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import registerstion_view ,logout_view


urlpatterns = [
    path('login/', obtain_auth_token, name ='login'),
    path('register/', logout_view, name ='register'),
    path('logout/', registerstion_view, name ='logout'),
    
]

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from user_app.api.serializers import RegisterationSerializer
from user_app import models



@api_view(['POST',])
def registerstion_view(request):

    if request.method == 'POST':
        serializer = RegisterationSerializer(data=request.data)
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = "Registeration successful"
            data['username'] = account.username   
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
            
        else:
            data = serializer.errors
            
        return Response(data)
        
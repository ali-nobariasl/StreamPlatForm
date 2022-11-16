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
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
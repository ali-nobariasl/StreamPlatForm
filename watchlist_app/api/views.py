from rest_framework.response import Response
from rest_framework import status , viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist_app.models import WatchList, StreamPlatform , Review
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins

from watchlist_app.models import StreamPlatform ,WatchList , Review 
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer



@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = WatchList.objects.all() 
        serialize = WatchListSerializer(movies, many= True)
        return Response(serialize.data)
    
    if request.method == 'POST':
        serialize = WatchListSerializer(data= request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)
        

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    try :
        movie = WatchList.objects.get(pk = pk)
    except WatchList.DoesNotExist:
        return Response({'Error':'ther is no movie for this number baby :D '})
        
    serialize = WatchListSerializer(movie)
    return Response(serialize.data)


@api_view(['GET', 'POST'])
def platform_list (request):
    if request.method == 'GET':
        plat = StreamPlatform.objects.all()
        serialize = StreamPlatformSerializer(plat, many=True)
        return Response(serialize.data)
    
    if request.method == 'POST':
        serialize = StreamPlatformSerializer(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)
        
@api_view(['GET', 'PUT','DELETE'])
def platform_Detail (request, pk):
    try:
        plat = StreamPlatform.objects.get(pk =pk)
    except StreamPlatform.DoesNotExist:
        return Response({'Error':'Movie Not found :D '})
        
    if request.method == 'GET':
        serialize = StreamPlatformSerializer(plat)
        return Response(serialize.data)
    
    if request.method == 'PUT':
        serialize = StreamPlatformSerializer( plat ,data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)
        
    if request.method == 'DELETE':
        plat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
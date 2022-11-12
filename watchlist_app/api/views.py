from rest_framework.response import Response
from rest_framework import status , viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist_app.models import WatchList, StreamPlatform , Review
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins

from watchlist_app.models import StreamPlatform ,WatchList , Review 
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer



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
        
    if request.method == 'GET':
        serialize = WatchListSerializer(movie)
        return Response(serialize.data)
    if request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        serialize = WatchListSerializer(movie, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)


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


class Platform_detailAv(APIView):
    
    def get(self, request,pk):
        try:
            plat = StreamPlatform.objects.get(pk =pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'platform not found'})
        
        serialize = StreamPlatformSerializer(plat)
        return Response(serialize.data)
    
    def delete(self, request,pk):
        try:
            plat = StreamPlatform.objects.get(pk =pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'platform not found'})
        plat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self,request,pk):
        try:
            plat = StreamPlatform.objects.get(pk =pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'platform not found'})
        
        serialize = StreamPlatformSerializer(plat, data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)
        

class Platform_listAv(APIView):
    def get(self, request):
        plat = StreamPlatform.objects.all()
        serialize = StreamPlatformSerializer(plat, many=True)
        return Response(serialize.data)
    
    def post(self,request):
        serialize = StreamPlatformSerializer(data= request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)
    
    
class Movie_listAv(APIView):
    
    def post(self,request):
        serialize = WatchListSerializer(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)
        
    def get(self,request):
        movie = WatchList.objects.all()
        serialize = WatchListSerializer(movie, many= True)
        return Response(serialize.data)
    
    
class Movie_detailAv(APIView):
    
    def get(self,request,pk ):
        try:
            movie = WatchList.objects.get(pk =pk)
        except WatchList.DoesNotExist:
            return Response({'Error':'Movie Not found :D '})
        
        serialize = WatchListSerializer(movie)
        return Response(serialize.data)
    
    def delete(self,request, pk):
        try:
            movie = WatchList.objects.get(pk =pk)
        except WatchList.DoesNotExist:
            return Response({'Error':'Movie Not found :D '})
        
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self,request,pk):
        try:
            movie = WatchList.objects.get(pk =pk)
        except WatchList.DoesNotExist:
            return Response({'Error':'Movie Not found :D '})
        
        serialize = WatchListSerializer(movie, data= request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)
        

class Review_detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin, generics.GenericAPIView):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class Review_list(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#class PlatfromVS(viewsets.Viewset):
    


from rest_framework.response import Response
from rest_framework import status , viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.throttling import UserRateThrottle , AnonRateThrottle
from django.shortcuts import get_object_or_404


from watchlist_app.models import StreamPlatform ,WatchList , Review 
from watchlist_app.api.permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
from watchlist_app.api.throttling import ReviewCreateThrottle ,ReviewListThrottle
from watchlist_app.api.pagination import WatchListPagination

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
    permission_classes = [IsAdminOrReadOnly]
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
    permission_classes = [IsAdminOrReadOnly]
    #permission_classes = [IsAuthenticated]
    
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
    permission_classes = [IsAdminOrReadOnly]
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
    permission_classes = [IsAdminOrReadOnly]
    
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


class Review_detailGv(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsReviewUserOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class Review_listGv(generics.ListAPIView):
    pagination_class = [IsAuthenticated]
    throttle_classes = [ReviewListThrottle, AnonRateThrottle]
    #queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(WatchList = pk)


class Platform_Viewset(viewsets.ViewSet):
    permission_classes = [IsAdminOrReadOnly]
    
    def list(self, request):
        query_set = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(query_set,many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        query_set = StreamPlatform.objects.all()
        watchlist = get_object_or_404(query_set, pk=pk)
        serializer = StreamPlatformSerializer(watchlist)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = StreamPlatformSerializer(data = request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)   


        
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewCreateThrottle]
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        
        review_user = self.request.user
        obj = Review.objects.filter(WatchList=watchlist, review_user =review_user)
        if obj.exists():
            raise ValidationError("you have  already reviewed this one :D ")
        
        if watchlist.number_rating == 0:
            watchlist.Avr_rate == serializer.validated_data['rating']
        else:
            watchlist.Avr_rate == (watchlist.Avr_rate + serializer.validated_data['rating']) /2 
            
        watchlist.number_rating += 1
        watchlist.save()
        serializer.save(WatchList= watchlist, review_user=review_user)
        

class UserReview(generics.ListAPIView):
    serializer_class = ReviewSerializer
    
#    def get_queryset(self):
#        username = self.kwargs['username']
#        return Review.objects.filter(review_user__username=username)

    def get_queryset(self):
        username = self.request.query_params.get('username',None)
        return Review.objects.filter(review_user__username=username)
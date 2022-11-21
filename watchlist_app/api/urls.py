from rest_framework.routers import DefaultRouter
from django.urls import path , include

from watchlist_app.api.views import (movie_list , movie_detail, platform_list , platform_Detail ,
                                     Movie_detailAv , Movie_listAv , Platform_listAv, Platform_detailAv,
                                     Review_detail , Review_list ,
                                     Review_detailGv, Review_listGv,
                                     Platform_Viewset,
                                     ReviewCreate,
                                     UserReview,
                                     MovieListALI
                                       )



router = DefaultRouter()
router.register( 'stream', Platform_Viewset, basename='Platform-Viewset')

urlpatterns = [
  
    path('', MovieListALI.as_view(), name = 'movie-list'),
    path('<int:pk>/', Movie_detailAv.as_view(), name = 'movie-detail'),
    
    #path('stream/', Platform_listAv.as_view(), name = 'platform-list'),
    #path('stream/<int:pk>/', Platform_detailAv.as_view(), name = 'platform-Detail'),
    
    path('review/<int:pk>/', Review_detailGv.as_view(), name = 'Review_detail'),
    path('<int:pk>/reviews/', Review_listGv.as_view(), name = 'Review_detail'),
    path('<int:pk>/review/create', ReviewCreate.as_view(), name = 'Review_detail'),
    
    #path('reviews/<str:username>/', UserReview.as_view(), name = 'user-review-detail'),
    path('reviews/', UserReview.as_view(), name = 'user-review-detail'),

    path('', include(router.urls)), 
    
]
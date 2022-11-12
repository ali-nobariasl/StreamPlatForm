from rest_framework.routers import DefaultRouter
from django.urls import path , include

from watchlist_app.api.views import (movie_list , movie_detail, platform_list , platform_Detail ,
                                     Movie_detailAv , Movie_listAv , Platform_listAv, Platform_detailAv,
                                     Review_detail , Review_list ,
                                     Review_detailGv, Review_listGv,
                                     Platform_Viewset
                                       )



router = DefaultRouter()
router.register( 'stream', Platform_Viewset, basename='Platform-Viewset')

urlpatterns = [
    path('list/', Movie_listAv.as_view(), name = 'movie-list'),
    path('list/<int:pk>/', Movie_detailAv.as_view(), name = 'movie-detail'),
    
    path('platlist/', Platform_listAv.as_view(), name = 'platform-list'),
    path('platlist/<int:pk>/', Platform_detailAv.as_view(), name = 'platform-Detail'),
    
    path('rewlist/<int:pk>/', Review_detailGv.as_view(), name = 'Review_detail'),
    path('rewlist/', Review_listGv.as_view(), name = 'Review_detail'),
    
    path('', include(router.urls)), 
    
]
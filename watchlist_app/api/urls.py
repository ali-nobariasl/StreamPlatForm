from django.urls import path , include

from watchlist_app.api.views import (movie_list , movie_detail, platform_list , platform_Detail ,
                                     Movie_detailAv , Movie_listAv , Platform_listAv, Platform_detailAv,
                                     Review_detail , Review_list
                                       )






urlpatterns = [
    path('list/', Movie_listAv.as_view(), name = 'movie-list'),
    path('list/<int:pk>/', Movie_detailAv.as_view(), name = 'movie-detail'),
    
    path('platlist/', Platform_listAv.as_view(), name = 'platform-list'),
    path('platlist/<int:pk>/', Platform_detailAv.as_view(), name = 'platform-Detail'),
    
    path('rewlist/<int:pk>/', Review_detail.as_view(), name = 'Review_detail'),
    path('rewlist/', Review_list.as_view(), name = 'Review_detail'),
    
]
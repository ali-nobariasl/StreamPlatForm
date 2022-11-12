from django.urls import path , include

from watchlist_app.api.views import (movie_list , movie_detail, platform_list , platform_Detail ,
                                     Movie_detailAv , Movie_listAv , platform_listAv, platform_detailAv
                                       )






urlpatterns = [
    path('list/', Movie_listAv.as_view(), name = 'movie-list'),
    path('list/<int:pk>/', Movie_detailAv.as_view(), name = 'movie-detail'),
    
    path('platlist/', platform_listAv.as_view(), name = 'platform-list'),
    path('platlist/<int:pk>/', platform_detailAv.as_view(), name = 'platform-Detail'),
    
]
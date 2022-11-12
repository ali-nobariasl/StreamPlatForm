from django.urls import path , include

from watchlist_app.api.views import movie_list , movie_detail, platform_list , platform_Detail

urlpatterns = [
    path('list/', movie_list, name = 'movie-list'),
    path('list/<int:pk>/', movie_detail, name = 'movie-detail'),
    
    path('platlist/', platform_list, name = 'platform-list'),
    path('platlist/<int:pk>', platform_Detail, name = 'platform-Detail'),
    
]
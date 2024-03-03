
from django.urls import path
from . import views

urlpatterns = [
    # path('list/', views.movie_list, name='movie-list'),
    # path('list/<int:pk>', views.movie_detail, name='movie-detail'),
    #  path('stream/', views.stream_list, name='stream-platform'),
    # path('stream/<int:pk>', views.stream_detail, name='stream-platform-detail'),
# class base views urls---------------
    # ------to use hyperlink serializer as bas class , urls must be in this format modelName-list/detail
    path('streamPlatform/', views.StreamPlatformList.as_view(), name='Streamplatform-list'),
    path('streamPlatform/<int:pk>', views.StreamPlatformDetail.as_view(), name='streamplatform-detail'),
    path('watchList/', views.watchListList.as_view(), name='watchlist-list'),
    path('watchList/<int:pk>', views.watchListDetail.as_view(), name='watchlist-detail'),
    path('',views.api_root),
    

]

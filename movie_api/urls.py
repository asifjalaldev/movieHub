
from django.urls import path
from . import views

urlpatterns = [
    # path('list/', views.movie_list, name='movie-list'),
    # path('list/<int:pk>', views.movie_detail, name='movie-detail'),
    #  path('stream/', views.stream_list, name='stream-platform'),
    # path('stream/<int:pk>', views.stream_detail, name='stream-platform-detail'),
# class base views urls---------------
    path('stream/', views.Stream.as_view(), name='stream-platform'),
    path('stream/<int:pk>', views.StreamDetail.as_view(), name='stream-detail'),
    path('list/', views.watchListView.as_view(), name='movie-list'),
    path('list/<int:pk>', views.watchListDetailView.as_view(), name='movie-detail'),
    path('',views.api_root),
    

]

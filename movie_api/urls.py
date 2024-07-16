
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
# using routers for viewsets
router=DefaultRouter()
router.register(r'streamplatforms', views.streamPlatformVeiwsets, basename='streamplatform')
router.register(r'watchlists', views.WatchListViewSet, basename='watchlist')
# router.register(r'')
urlpatterns = [
    # path('list/', views.movie_list, name='movie-list'),
    # path('list/<int:pk>', views.movie_detail, name='movie-detail'),
    #  path('stream/', views.stream_list, name='stream-platform'),
    # path('stream/<int:pk>', views.stream_detail, name='stream-platform-detail'),
# class base views urls---------------
    # ------to use hyperlink serializer as bas class , urls must be in this format modelname-list/detail with all 'lowercase', even not camel case accepted
    # path('streamPlatform/', views.StreamPlatformList.as_view(), name='Streamplatform-list'),
    # path('streamPlatform/<int:pk>', views.StreamPlatformDetail.as_view(), name='streamplatform-detail'),
    # path('watchList/', views.watchListList.as_view(), name='watchlist-list'),
    # path('watchList/<int:pk>', views.watchListDetail.as_view(), name='watchlist-detail'),
    # path('',views.api_root),
    path('', include(router.urls)),
    # path('review/', views.ReviewListView.as_view(), name='Review-list'),
    # path('review/<int:pk>', views.ReviewListDetailView.as_view(), name='Review-detail'),
    path('watchlists/<int:pk>/review', views.ReviewListView.as_view(), name='Review-list'),

    path('watchlists/<int:pk>/review/create', views.ReviewCreateView.as_view(), name='review-create'),



    path('watchlists/review/<int:pk>', views.ReviewListDetailView.as_view(), name='review-detail'),



]
print('url are called')
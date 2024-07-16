from django.urls import path
from .views import myView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'posts', myView, basename='posts')
urlpatterns = [
    # path('', myView.as_view(), name='myview'),

]
urlpatterns=router.urls
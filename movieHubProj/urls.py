
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movie_api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
        # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwMTc1MTgxLCJpYXQiOjE3MTAxNzQ4ODEsImp0aSI6IjkzYjRkYjU4N2NhNTRmOGRhMzVkYTRjMjAzZmYxY2E5IiwidXNlcl9pZCI6Mn0.2H5loI_vtph0D-ZQKghKo-GZ7e2pidZubKSCw7wVkFM
]

from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('refresh-token/', refresh_jwt_token, name='refresh-token'),
    path('verify-token/', verify_jwt_token, name='verify-token'),
]
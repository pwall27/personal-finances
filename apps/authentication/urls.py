from django.urls import path

from .views import MyTokenObtainPairView, MyTokenRefreshView

urlpatterns = [
    path('/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
]

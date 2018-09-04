from django.urls import path

from .views import TransactionViewSet

urlpatterns = [
    path('', TransactionViewSet.as_view({'get': 'list', 'post': 'create'}), name='transactions'),
]

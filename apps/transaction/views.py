from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import GenericViewSet

from .serializers import TransactionSerializer
from .models import Transaction


class TransactionViewSet(CreateAPIView, ListAPIView, GenericViewSet,):
    """
    A simple ModelViewSet for listing or creating new transactions.
    """

    serializer_class = TransactionSerializer
    filter_fields = ('amount', 'description')
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    pagination_class = None

    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user).all()

    def get_serializer_context(self):
        context = super(TransactionViewSet, self).get_serializer_context()
        context.update(
            {
                'owner': self.request.user
            }
        )
        return context

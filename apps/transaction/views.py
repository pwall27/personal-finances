from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import TransactionSerializer
from .models import Transaction


class TransactionViewSet(ViewSet):
    """
    A simple ViewSet for listing or inserting transactions.
    """

    def create(self, request):
        serializer = TransactionSerializer(data=request.data, context={'owner': self.request.user})
        serializer.is_valid(True)
        serializer.save()
        return Response(serializer.data)

    def list(self, request):
        queryset = Transaction.objects.filter(owner=self.request.user).all()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)

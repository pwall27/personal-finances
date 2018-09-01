from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.user.models import User
from .models import Transaction


class TransactionSerializer(ModelSerializer):
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), required=False, slug_field='uuid')

    class Meta:
        model = Transaction
        fields = ('uuid', 'description', 'amount', 'transaction_type', 'owner', 'created_at', 'updated_at')
        read_only_fields = ('uuid', 'created_at', 'updated_at')

    def validate(self, attrs=None, *args, **kwargs):
        attrs.update({
            'owner': self.context.get('owner')
        })
        return super(TransactionSerializer, self).validate(attrs)

from babel.numbers import format_currency
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.user.models import User
from .models import Transaction


class AmountField(serializers.DecimalField):
    def to_representation(self, obj):
        return format_currency(obj, currency="BRL", locale="pt_BR")


class TransactionSerializer(ModelSerializer):
    owner = serializers.SlugRelatedField(
        queryset=User.objects.all(), required=False, slug_field='uuid', write_only=True
    )

    amount = AmountField(max_digits=8, decimal_places=2)

    class Meta:
        model = Transaction
        fields = ('description', 'amount', 'transaction_type', 'owner',)

    def validate(self, attrs=None, *args, **kwargs):
        attrs.update({
            'owner': self.context.get('owner')
        })
        return super(TransactionSerializer, self).validate(attrs)

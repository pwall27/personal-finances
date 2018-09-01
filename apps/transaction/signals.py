from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from .models import Transaction


@receiver(pre_save, sender=Transaction)
def validate_expense(sender, instance: Transaction, **kwargs):
    if instance.transaction_type == Transaction.EXPENSE_TYPE and instance.amount > 0:
        instance.amount = instance.amount * -1


@receiver(pre_save, sender=Transaction)
def validate_earning(sender, instance: Transaction, **kwargs):
    if instance.transaction_type == Transaction.EARNING_TYPE and instance.amount < 0:
        raise ValidationError({'message': _('Earning amount should be a positive number.')})

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Transaction


@receiver(pre_save, sender=Transaction)
def validate_expense(sender, instance: Transaction, **kwargs):
    if instance.transaction_type == Transaction.EXPENSE_TYPE and instance.amount > 0:
        instance.amount = instance.amount * -1

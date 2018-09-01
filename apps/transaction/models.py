import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Transaction(models.Model):
    EARNING_TYPE = 'earning'
    EXPENSE_TYPE = 'expense'
    TRANSACTION_TYPES = (
        (EARNING_TYPE, _('Earning')),
        (EXPENSE_TYPE, _('Expense'))
    )

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, null=False, blank=False, unique=True)
    description = models.CharField(_('Description'), max_length=150, null=False, blank=False)
    amount = models.DecimalField(_('Amount'), max_digits=8, decimal_places=2, null=False, blank=False)
    transaction_type = models.CharField(
        _('Type'), max_length=10, null=False, blank=False, choices=TRANSACTION_TYPES, default=EARNING_TYPE
    )
    owner = models.ForeignKey('user.User', models.CASCADE, 'transactions', null=False)

    created_at = models.DateTimeField(_('Created Date'), auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(_('Updated Date'), auto_now=True, null=True, blank=False)

    def __str__(self):
        return f"{self.owner}: {self.amount}"

    class Meta:
        app_label = 'transaction'
        db_table = 'transactions'
        ordering = ('created_at',)
        verbose_name = _('Transaction')
        verbose_name_plural = _('Transactions')

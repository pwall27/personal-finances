from django.apps import AppConfig


class TransactionConfig(AppConfig):
    name = 'apps.transaction'

    def ready(self):
        from . import signals

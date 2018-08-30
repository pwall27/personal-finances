from django.contrib.auth.base_user import BaseUserManager
from django.db import transaction


class UserManager(BaseUserManager):

    @transaction.atomic
    def create_user(self, email=None, password=None, **kwargs):
        confirm_password = kwargs.pop('confirm_password') if kwargs.get('confirm_password') else None

        user = self.model(
            email=email,
            **kwargs
        )

        password = user.validate_password(password, confirm_password)
        user.set_password(password)
        user.save()
        return user

    @transaction.atomic
    def create_superuser(self, email=None, password=None, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_staff = True
        user.is_verified = True
        user.save()
        return user

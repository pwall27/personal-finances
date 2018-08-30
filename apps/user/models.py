import uuid

from django.contrib.auth import password_validation
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError as DjangoValidationError

from rest_framework.exceptions import ValidationError

from .managers import UserManager


class User(AbstractBaseUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, null=False, blank=False, unique=True)
    email = models.EmailField(_('Email'), null=False, blank=False, unique=True)
    name = models.CharField(_('Name'), max_length=150, null=True, blank=True)

    is_active = models.BooleanField(_('Is Active?'), default=True)
    is_staff = models.BooleanField(_('Is Staff?'), default=False)
    is_verified = models.BooleanField(_('Is Verified?'), default=False)

    created_at = models.DateTimeField(_('Created Date'), auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(_('Updated Date'), auto_now=True, null=True, blank=False)

    def __str__(self):
        return self.email

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        app_label = 'user'
        db_table = 'users'
        ordering = ('created_at',)
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        abstract = False

    def validate_password(self, password, confirm_password=None):
        if confirm_password and confirm_password != password:
            raise ValidationError({"message": _("Passwords don't match.")})
        try:
            password_validation.validate_password(password, self)
        except DjangoValidationError as e:
            raise ValidationError({"message": " ".join(e.messages)})
        return password

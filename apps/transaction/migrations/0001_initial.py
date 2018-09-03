# Generated by Django 2.1.1 on 2018-09-01 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('description', models.CharField(max_length=150, verbose_name='Description')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Amount')),
                ('transaction_type', models.CharField(choices=[('earning', 'Earning'), ('expense', 'Expense')], default='earning', max_length=10, verbose_name='Type')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Date')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
                'db_table': 'transactions',
                'ordering': ('created_at',),
            },
        ),
    ]
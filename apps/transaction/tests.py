from random import choice

from mixer.backend.django import mixer
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model
from faker import Faker
from rest_framework import status
from rest_framework.test import APIClient

from apps.transaction.models import Transaction

User = get_user_model()


class TransactionUnitTests(TestCase):

    def setUp(self):
        self.fake = Faker()
        email = self.fake.email()
        password = self.fake.password(
            length=10, special_chars=True, digits=True, upper_case=True, lower_case=True
        )
        self.user = User.objects.create_user(email, password, is_verified=True)

    def test_register_an_earning(self):
        data = {
            'owner': self.user,
            'transaction_type': Transaction.EARNING_TYPE,
            'amount': self.fake.pydecimal(left_digits=3, right_digits=2, positive=True),
            'description': self.fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        }
        transaction = Transaction.objects.create(**data)
        self.assertEqual(data['owner'], transaction.owner)
        self.assertEqual(data['transaction_type'], transaction.transaction_type)
        self.assertEqual(data['amount'], transaction.amount)
        self.assertEqual(data['description'], transaction.description)
        self.assertIsNotNone(transaction.uuid)
        self.assertIsNotNone(transaction.id)

    def test_register_an_expense(self):
        data = {
            'owner': self.user,
            'transaction_type': Transaction.EXPENSE_TYPE,
            'amount': self.fake.pydecimal(left_digits=3, right_digits=2, positive=True) * -1,
            'description': self.fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        }
        transaction = Transaction.objects.create(**data)
        self.assertEqual(data['owner'], transaction.owner)
        self.assertEqual(data['transaction_type'], transaction.transaction_type)
        self.assertEqual(data['amount'], transaction.amount)
        self.assertEqual(data['description'], transaction.description)
        self.assertIsNotNone(transaction.uuid)
        self.assertIsNotNone(transaction.id)

    def test_register_an_expense_positive_amount(self):
        data = {
            'owner': self.user,
            'transaction_type': Transaction.EXPENSE_TYPE,
            'amount': self.fake.pydecimal(left_digits=3, right_digits=2, positive=True),
            'description': self.fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        }
        transaction = Transaction.objects.create(**data)
        self.assertEqual(data['owner'], transaction.owner)
        self.assertEqual(data['transaction_type'], transaction.transaction_type)
        self.assertEqual(data['amount'] * -1, transaction.amount)
        self.assertEqual(data['description'], transaction.description)
        self.assertIsNotNone(transaction.uuid)
        self.assertIsNotNone(transaction.id)

    def test_register_an_earning_negative_amount(self):
        data = {
            'owner': self.user,
            'transaction_type': Transaction.EARNING_TYPE,
            'amount': self.fake.pydecimal(left_digits=3, right_digits=2, positive=True) * -1,
            'description': self.fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        }
        with self.assertRaises(ValidationError):
            Transaction.objects.create(**data)


class TransactionAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.fake = Faker()
        email = self.fake.email()
        password = self.fake.password(
            length=10, special_chars=True, digits=True, upper_case=True, lower_case=True
        )

        self.user = User.objects.create_user(email, password, is_verified=True)
        response = self.client.post(
            f'/api/v1/auth/login/', {'email': email, 'password': password}, format='json'
        )
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data.get('access_token'))

    def test_register_earning(self):
        data = {
            'transaction_type': Transaction.EARNING_TYPE,
            'amount': self.fake.pydecimal(left_digits=3, right_digits=2, positive=True),
            'description': self.fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        }
        response = self.client.post(
            f'/api/v1/transactions/', data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['transaction_type'], data['transaction_type'])
        self.assertEqual(response.data['amount'], data['amount'])
        self.assertEqual(response.data['description'], data['description'])
        self.assertEqual(response.data['owner'], self.user.uuid)

    def test_register_expense(self):
        data = {
            'transaction_type': Transaction.EXPENSE_TYPE,
            'amount': self.fake.pydecimal(left_digits=3, right_digits=2, positive=True),
            'description': self.fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        }
        response = self.client.post(
            f'/api/v1/transactions/', data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['transaction_type'], data['transaction_type'])
        self.assertEqual(response.data['amount'], data['amount'] * -1)
        self.assertEqual(response.data['description'], data['description'])
        self.assertEqual(response.data['owner'], self.user.uuid)

    def test_register_expense_for_another_user(self):
        another_user = User.objects.create_user(
            email=self.fake.email(),
            password=self.fake.password(
                length=10, special_chars=True, digits=True, upper_case=True, lower_case=True
            ),
            is_verified=True
        )
        data = {
            'transaction_type': Transaction.EXPENSE_TYPE,
            'amount': self.fake.pydecimal(left_digits=3, right_digits=2, positive=True),
            'description': self.fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None),
            'owner': another_user.uuid
        }
        response = self.client.post(
            f'/api/v1/transactions/', data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['transaction_type'], data['transaction_type'])
        self.assertEqual(response.data['amount'], data['amount'] * -1)
        self.assertEqual(response.data['description'], data['description'])
        self.assertEqual(response.data['owner'], self.user.uuid)

    def test_register_transaction_without_body(self):
        data = {
        }
        response = self.client.post(
            f'/api/v1/transactions/', data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_transactions(self):
        list_size = 15
        for x in range(list_size):
            Transaction.objects.create(**{
                'owner': self.user,
                'transaction_type': choice([Transaction.EARNING_TYPE, Transaction.EXPENSE_TYPE]),
                'amount': self.fake.pydecimal(left_digits=3, right_digits=2, positive=True),
                'description': self.fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
            })
        response = self.client.get(
            f'/api/v1/transactions/'
        )
        self.assertEqual(len(response.data), list_size)

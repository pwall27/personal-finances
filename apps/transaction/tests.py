from django.test import TestCase
from django.contrib.auth import get_user_model
from faker import Faker

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

    def test_register_a_earning_transaction(self):
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

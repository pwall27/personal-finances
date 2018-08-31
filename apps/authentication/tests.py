from faker import Faker
from rest_framework import status

from rest_framework.test import APIClient

from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthenticationAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.fake = Faker()
        self.email = self.fake.email()
        self.password = self.fake.password(
            length=10, special_chars=True, digits=True, upper_case=True, lower_case=True
        )

        self.user = User.objects.create_user(self.email, self.password)
        self.user.is_verified = True
        self.user.save()

    def test_login_right_credentials(self):
        response = self.client.post(
            f'/api/v1/auth/login/', {'email': self.email, 'password': self.password, }, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_wrong_email(self):
        response = self.client.post(
            f'/api/v1/auth/login/', {'email': self.fake.email(), 'password': self.password}, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_wrong_password(self):
        response = self.client.post(
            f'/api/v1/auth/login/',
            {
                'email': self.email,
                'password': self.fake.password(
                    length=10, special_chars=True, digits=True, upper_case=True, lower_case=True
                ),
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_without_credentials(self):
        response = self.client.post(
            f'/api/v1/auth/login/', {},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_without_email(self):
        response = self.client.post(
            f'/api/v1/auth/login/', {'password': self.password,},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_without_password(self):
        response = self.client.post(
            f'/api/v1/auth/login/', {'email': self.email,},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

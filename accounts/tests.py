from django.test import TestCase
from django.contrib.auth import get_user_model


class AccountsTests(TestCase):
    def setUp(self) -> None:
        self.user: get_user_model() = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@test.com'
        )

    def test_login_get_request(self):
        response = self.client.get('/accounts/login/')
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertEqual(response.status_code, 200)

    def test_login_with_real_user(self):
        login_status: bool = self.client.login(
            username='testuser', password='testpassword')
        self.assertEqual(login_status, True)

    def test_login_with_wrong_user(self):
        login_status: bool = self.client.login(
            username='wronguser', password='wrongpassword')
        self.assertEqual(login_status, False)

    def test_register(self):
        response_get = self.client.get('/accounts/register/')
        response_post = self.client.post('/accounts/register/',
                                         {'username': 'test-user', 'password': 'testpasswd', 'email': 'info@test.com'})
        self.assertTemplateUsed(response_get, 'registration/register.html')
        self.assertEqual(response_post.status_code, 200)

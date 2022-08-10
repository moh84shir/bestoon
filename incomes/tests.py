from django.test import TestCase
from .models import Income
from django.contrib.auth import get_user_model
from django.urls import reverse


class IncomeModelTests(TestCase):
    def setUp(self) -> None:
        self.user: get_user_model() = get_user_model().objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpassword'
        )

        self.income: Income = Income.objects.create(
            text='testincometext',
            amount=1234,
            user=self.user
        )

    def test_income_user(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@test.com')

    def test_income_model(self):
        self.assertEqual(self.income.text, 'testincometext')
        self.assertEqual(self.income.amount, 1234)
        self.assertEqual(self.income.user, self.user)

    def test_income_text(self):
        income: Income = Income(text='test text')
        self.assertEqual(str(income), income.text)

    def test_income_list(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('incomes:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'incomes/income_list.html')

    def test_income_detail(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('incomes:detail', kwargs={'pk': self.income.pk}))
        no_response = self.client.get(
            reverse('incomes:detail', kwargs={'pk': 10}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(
            response, 'incomes/income_detail.html')

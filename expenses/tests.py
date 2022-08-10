from django.test import TestCase
from .models import Expense
from django.contrib.auth import get_user_model
from django.urls import reverse


class ExpenseModelTests(TestCase):
    def setUp(self) -> None:
        self.user: get_user_model() = get_user_model().objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpassword'
        )

        self.expense: Expense = Expense.objects.create(
            text='testexpensetext',
            amount=1234,
            user=self.user
        )

    def test_expense_user(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@test.com')

    def test_expense_model(self):
        self.assertEqual(self.expense.text, 'testexpensetext')
        self.assertEqual(self.expense.amount, 1234)
        self.assertEqual(self.expense.user, self.user)

    def test_expense_text(self):
        self.client.force_login(self.user)
        expense: Expense = Expense(text='testexpensetext')
        self.assertEqual(str(expense), expense.text)

    def test_expense_list(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('expenses:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'expenses/expense_list.html')

    def test_expense_detail(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('expenses:detail', kwargs={'pk': self.expense.pk}))
        no_response = self.client.get(
            reverse('expenses:detail', kwargs={'pk': 10}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(
            response, 'expenses/expense_detail.html')


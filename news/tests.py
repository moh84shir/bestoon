from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import News


class NewsModelTests(TestCase):
    def setUp(self) -> None:
        self.user: get_user_model() = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            email='info@test.com'
        )

        self.news: News = News.objects.create(
            title='test title',
            text='test text',
            is_active=True,
        )

    def test_news_model(self):
        self.assertEqual(self.news.title, 'test title')
        self.assertEqual(self.news.text, 'test text')
        self.assertEqual(self.news.is_active, True)

    def test_news_str_method(self):
        self.assertEqual(self.news.title, self.news.__str__())

    def test_news_list(self):
        response = self.client.get(reverse('news:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news_list.html')

    def test_news_detail(self):
        response = self.client.get(
            reverse('news:detail', kwargs={'pk': self.news.pk}))
        no_response = self.client.get(
            reverse('news:detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'news/news_detail.html')

    def test_news_gau(self):  # gau => get absolute url
        news_detail_url_from_gau_method = self.news.get_absolute_url()
        custom_news_detail_url = reverse(
            'news:detail', kwargs={'pk': self.news.pk})
        self.assertEqual(news_detail_url_from_gau_method,
                         custom_news_detail_url)

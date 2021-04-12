from django.test import TestCase
from django.contrib.auth.models import User
from .models import Portfolio
import json


# Create your tests here.
class PortfolioTestCase(TestCase):

    def test_list_portfolio_status(self):
        url = '/gallery/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_count_portfolio_list(self):
        user_model = User.objects.create_user(username='test', password='pass', first_name='test', last_name='test',
                                              email='email')
        Portfolio.objects.create(product='test', user=user_model, public=True)
        Portfolio.objects.create(product='test', user=user_model, public=False)
        response = self.client.get('/gallery/')
        current_data = json.loads(response.content)
        self.assertEqual(len(current_data), 2)

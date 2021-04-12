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

    def test_add_user(self):
        response = self.client.post('/gallery/addUser/', json.dumps(
            {'username': 'testUser', 'first_name': 'Test', 'last_name': 'User', 'password': 'AnyPass',
             'email': 'prueba@gmail.com'}), content_type='application/json')
        current_data = json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['username'], 'testUser')

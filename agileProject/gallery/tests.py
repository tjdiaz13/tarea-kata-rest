from django.test import TestCase


# Create your tests here.
class PortfolioTestCase(TestCase):

    def test_list_portfolio_status(self):
        url = '/gallery/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

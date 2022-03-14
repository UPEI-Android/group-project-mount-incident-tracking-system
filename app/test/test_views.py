from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import authenticate


class TestViews(TestCase):
    def setUp(self):
        self.home_url = reverse('home')
        self.dashboard_url = reverse('dashboard')

        self.user = {
            'Username': 'Paakow',
            'Password': '1234'
        }
        self.anAuthUser = {
            'Username': '',
            'Password': ''
        }
        return super().setUp()

    """Test to validate login page"""
    def test_home_page(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    """Test to see if an authenticate user can access the dashboard after successful authentication """
    def test_can_login_user(self):
        response = self.client.post(self.dashboard_url, self.user, format='text/html')
        self.assertEquals(response.status_code, 302)

    """Test to see if unauthenticated users are redirected to login page"""
    def test_unauthenticated_user(self):
        response = self.client.post(self.home_url, self.anAuthUser, format='text/html')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

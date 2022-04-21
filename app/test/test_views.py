from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import authenticate

# test to check if the right templates are rendered for each view
class TestViews(TestCase):
    def setUp(self):
        self.home_url = reverse('home')
        self.dashboard_url = reverse('dashboard')
        self.form_url = reverse('form')
        self.logout_url = reverse('logout')
        self.dashboard_export_url = reverse('dashboard-export')
        self.edit_report_url = reverse('edit_report')

        self.user = {
            'Username': 'Paakow',
            'Password': '1234'
        }
        self.anAuthUser = {
            'Username': '',
            'Password': ''
        }
        return super().setUp()

    def test_home_page(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_form_page(self):
        response = self.client.get(self.form_url)
        self.assertEquals(response.status_code, 302)

    def test_dashboard_page(self):
        response = self.client.get(self.dashboard_url)
        self.assertEquals(response.status_code, 302)

    def test_logout_function(self):
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code, 302)

    def test_dashboard_export(self):
        response = self.client.get(self.dashboard_export_url)
        self.assertEquals(response.status_code, 302)

    def test_read_report(self):
        response = self.client.post(self.home_url, self.anAuthUser, format='text/html')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_edit_report(self):
        response = self.client.post(self.home_url, self.anAuthUser, format='text/html')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_signOff_report(self):
        response = self.client.post(self.home_url, self.anAuthUser, format='text/html')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_mark_as_complete(self):
        response = self.client.post(self.home_url, self.anAuthUser, format='text/html')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_can_login_user(self):
        response = self.client.post(self.dashboard_url, self.user, format='text/html')
        self.assertEquals(response.status_code, 302)

    def test_unauthenticated_user(self):
        response = self.client.post(self.home_url, self.anAuthUser, format='text/html')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_delete_report(self):
        response = self.client.post(self.home_url, self.anAuthUser, format='text/html')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


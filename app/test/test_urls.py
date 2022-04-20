from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import home, form, dashboard, logout_view, dashboard_export


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

    def test_form_url_is_resolved(self):
        url = reverse('form')
        print(resolve(url))
        self.assertEquals(resolve(url).func, form)

    def test_dashboard_url_is_resolved(self):
        url = reverse('dashboard')
        print(resolve(url))
        self.assertEquals(resolve(url).func, dashboard)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout_view)

    def test_dashboard_export_url_is_resolved(self):
        url = reverse('dashboard_export')
        print(resolve(url))
        self.assertEquals(resolve(url).func, dashboard_export)

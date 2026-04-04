from django.test import TestCase
from django.urls import reverse, resolve

from elibrary_app.views import home


class ElibraryURLsTest(TestCase):
    """    Тестируем URLs    """

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

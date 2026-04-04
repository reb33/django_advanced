from django.test import TestCase
from django.urls import reverse

from elibrary_app.models import Catalog


class CatalogViewTests(TestCase):
    """    Тест для представлений    """
    def test_book_list_view(self):
        """ Тестовый метод, позволяющий показать, что созданные нами книги корректно отображаются в нашем шаблоне. """
        Book_1 = Catalog.objects.create(
            title='Django for Beginners (2018)',
            ISBN='978-1-60309-0',
            author='John Doe',
            price=9.99,
            availability=True
        )

        Book_2 = Catalog.objects.create(
            title='Django for Professionals (2020)',
            ISBN='978-1-60309-3',
            author='Mary Doe',
            price=11.99,
            availability=False
        )

        response = self.client.get(reverse('home'))

        self.assertIn('Django for Professionals (2020)', response.content.decode())
        self.assertIn('John Doe', response.content.decode())
        self.assertIn('978-1-60309-3', response.content.decode())

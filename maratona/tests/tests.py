from django.test import TestCase, Client
from django.urls import reverse


class IndexViewTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def test_access_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
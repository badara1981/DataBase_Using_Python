from django.test import TestCase
from django.urls import reverse
from django.shortcuts import resolve_url

class MathTest(TestCase):
    def test_addition_operation(self):
        url = reverse('math')
        response = self.client.get(f"{url}?operation=add&a=1&b=2")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "3")

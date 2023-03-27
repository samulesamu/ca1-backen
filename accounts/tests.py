from django.test import TestCase
from django.urls import reverse, resolve
# Create your tests here.


class SignUpTests(TestCase):

    # test add subject page
    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

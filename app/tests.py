from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class RecompensasViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('recompensas'))
        self.assertRedirects(response, '/login/?next=/recompensas/')

    def test_logged_in_access(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('recompensas'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recompensas.html')

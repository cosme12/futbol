from django.test import TestCase

# Create your tests here.


class HomePageTest(TestCase):

    def test_home_redirect(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], 'login/?next=/')

    def test_uses_login_template(self):
        response = self.client.get('/login/')
        print(response.status_code)
        self.assertTemplateUsed(response, 'registration/login.html')


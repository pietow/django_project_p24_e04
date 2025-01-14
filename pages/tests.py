from django.test import SimpleTestCase
from django.urls import reverse

class HomePageTests(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    # def test_url_available_by_name(self):
    #     response = self.client.get(reverse('my_home'))
    #     self.assertEqual(response.status_code, 200)

    # def test_template_name_correct(self):
    #     response = self.client.get(reverse('my_home'))
    #     self.assertTemplateUsed(response, 'home.html')

    # def test_template_content(self):
    #     response = self.client.get(reverse('my_home'))
    #     self.assertContains(response, '<h1>Home</h1>')



# class AboutPageTests(SimpleTestCase):
    # def test_url_exists(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)

    # def test_url_available_by_name(self):
    #     response = self.client.get(reverse('about'))
    #     self.assertEqual(response.status_code, 200)
    
    # def test_template_name_correct(self):
    #     response = self.client.get(reverse('about'))
    #     self.assertTemplateUsed(response, 'about.html')

    # def test_template_content(self):
    #     response = self.client.get(reverse('about'))
    #     self.assertContains(response, '<h1>About</h1>')
    #     self.assertIn(b'<h1>About</h1>', response.content)

from django.test import SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
    def test_home(self):
        respons=self.client.get('/')
        self.assertEqual(respons.status_code,200)
    def test_about(self):
        respons=self.client.get('/about/')
        self.assertEqual(respons.status_code,200)

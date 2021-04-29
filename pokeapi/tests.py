from django.test import TestCase


class TestPokemonApi(TestCase):

    def test_route(self):
        """Should return 200"""
        response = self.client.get('http://localhost:8000/pokemon/?name=ditto')
        self.assertEqual(200, response.status_code)

    def test_route_result(self):
        """Should return json"""
        response = self.client.get('http://localhost:8000/pokemon/?name=ditto')
        self.assertEqual(dict, type(response.json()))

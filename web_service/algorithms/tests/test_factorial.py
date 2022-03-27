from rest_framework import status
from rest_framework.test import APITestCase
from algorithms.helpers import prepare_response


class TestFactorial(APITestCase):
    url = "/api/factorial/"

    def test_200_ok_v1(self):
        query = "n=5"
        res = self.client.get(f"{self.url}?{query}")

        self.assertEqual(type(res.data), dict)
        self.assertEqual(res.data, prepare_response(120))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_200_ok_v2(self):
        query = "n=0"
        res = self.client.get(f"{self.url}?{query}")

        self.assertEqual(type(res.data), dict)
        self.assertEqual(res.data, prepare_response(1))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_400_negative_number(self):
        query = "n=-4"
        res = self.client.get(f"{self.url}?{query}")

        self.assertEqual(res.data, None)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_400_non_integer(self):
        query = "n=5se"
        res = self.client.get(f"{self.url}?{query}")

        self.assertEqual(res.data, None)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_400_special_char(self):
        query = "n=5*"
        res = self.client.get(f"{self.url}?{query}")

        self.assertEqual(res.data, None)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_405_method_not_allowed(self):
        query = "n=3"
        res = self.client.post(f"{self.url}?{query}")

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

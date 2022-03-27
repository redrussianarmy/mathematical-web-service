from rest_framework import status
from rest_framework.test import APITestCase
from algorithms.helpers import prepare_response


class TestAckermann(APITestCase):
    url = "/api/ackermann/"

    def test_200_ok_v1(self):
        query = "m=3&n=5"
        res = self.client.get(f"{self.url}?{query}")

        self.assertEqual(type(res.data), dict)
        self.assertEqual(res.data, prepare_response(253))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_200_ok_v2(self):
        query = "m=0&n=0"
        res = self.client.get(f"{self.url}?{query}")

        self.assertEqual(type(res.data), dict)
        self.assertEqual(res.data, prepare_response(1))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_400_negative_number_m(self):
        query = "m=-1&n=3"
        res = self.client.get(f"{self.url}?{query}")

        self.assertEqual(res.data, None)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_400_negative_number_n(self):
        query = "m=1&n=-3"
        res = self.client.get(f"{self.url}?{query}")

        self.assertEqual(res.data, None)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_400_non_integer_n(self):
        query = "m=1izmir&n=3"
        res = self.client.get(f"{self.url}?{query}")

        self.assertEqual(res.data, None)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_400_non_integer_n(self):
        query = "m=1&n=4plus"
        res = self.client.get(f"{self.url}?{query}")

        self.assertEqual(res.data, None)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_400_special_char(self):
        query = "m=1*&n=5"
        res = self.client.get(f"{self.url}?{query}")

        self.assertEqual(res.data, None)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_400_special_char(self):
        query = "m=1&n=7*"
        res = self.client.get(f"{self.url}?{query}")

        self.assertEqual(res.data, None)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_405_method_not_allowed(self):
        query = "m=1&n=2"
        res = self.client.post(f"{self.url}?{query}")

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

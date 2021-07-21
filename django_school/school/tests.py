from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import path, reverse


class StudentTestCase(APITestCase):
    def setUp(self):
        data = {"name": "Teacher", "gender": "M", "email": "test", "classroom": []}
        url = reverse("teacher_create")
        response = self.client.post(url, data, format="json")

    def test_create(self):
        data = {"name": "Test Student", "gender": "M", "grade": 96, "teacher": 1}
        url = reverse("student_create")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

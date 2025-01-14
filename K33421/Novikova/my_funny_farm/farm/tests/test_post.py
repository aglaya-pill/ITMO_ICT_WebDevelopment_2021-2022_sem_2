from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from ..models import *


class BreedCreateTest(TestCase):

    def test_breed_create(self):
        url = reverse('farm:breed_create')

        data = {
            'id': 1,
            'breed': 'very small chicken',
            'avg_eggs': 2,
            'avg_weight': 2,
            'diet': 'table 3'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), data)


class WorkerCreateTest(TestCase):

    def test_worker_create(self):
        url = reverse('farm:worker_create')

        data = {
            'id': 1,
            'name': 'Darya Kotelnikova',
            'passport': '1111 330044',
            'position': 'vet',
            'salary': 50000
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), data)


class ChickenCreateTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Breed.objects.create(breed='very small chicken',
                             avg_eggs=2,
                             avg_weight=2,
                             diet='table 3')

        Cage.objects.create(shed=2,
                            row=5,
                            cage=23,
                            square=30)

    def test_chicken_create(self):
        url = reverse('farm:chicken_create')

        data = {
            'id': 1,
            'breed': 1,
            'weight': 2,
            'age': 1,
            'egg_amount': 2,
            'cage': 1,
            'prev_eggs': 1
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), data)

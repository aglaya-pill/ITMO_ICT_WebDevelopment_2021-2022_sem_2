from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from ..models import *


class WorkerGetTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Worker.objects.create(name='Darya Kotelnikova',
                              passport='1111 330044',
                              position='vet',
                              salary=50000)

    def test_get_worker(self):
        url = reverse('farm:workers', args=['1'])
        data = {'id': 1,
                'name': 'Darya Kotelnikova',
                'passport': '1111 330044',
                'position': 'vet',
                'salary': 50000}
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)


class ChickenGetTest(TestCase):

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

        Chicken.objects.create(breed=Breed.objects.get(id=1),
                               weight=2,
                               age=1,
                               egg_amount=2,
                               cage=Cage.objects.get(id=1))

    def test_get_chicken(self):
        url = reverse('farm:chickens', args=['1'])
        data = {'id': 1,
                'breed': 1,
                'weight': 2,
                'age': 1,
                'egg_amount': 2,
                'cage': 1,
                'prev_eggs': 0}
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)


class ChickenBreedGetTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Breed.objects.create(id=1,
                             breed='very big chicken',
                             avg_eggs=7,
                             avg_weight=4,
                             diet='table 5')

        Breed.objects.create(id=2,
                             breed='very small chicken',
                             avg_eggs=2,
                             avg_weight=2,
                             diet='table 3')

        Cage.objects.create(shed=2,
                            row=6,
                            cage=21,
                            square=40)

        Chicken.objects.create(breed=Breed.objects.get(id=2),
                               weight=2,
                               age=3,
                               egg_amount=2,
                               cage=Cage.objects.get(id=1),
                               prev_eggs=1)

        Chicken.objects.create(id=2,
                               breed=Breed.objects.get(id=1),
                               weight=6,
                               age=2,
                               egg_amount=8,
                               cage=Cage.objects.get(id=1),
                               prev_eggs=7)

    def test_get_eggs_range_chicken(self):
        self.maxDiff = None
        url = reverse('farm:chickens_breed')
        data = {'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {'id': 1,
                     'breed': 'very small chicken',
                     'weight': 2,
                     'age': 3,
                     'egg_amount': 2,
                     'cage': '2 6 21',
                     'prev_eggs': 1
                     }
                ]}
        response = self.client.get(url, {'breed': '2'}, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
import json
from ..models import *


class BreedPutTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Breed.objects.create(breed='very small chicken',
                             avg_eggs=2,
                             avg_weight=2,
                             diet='table 3')

    def test_update_breed(self):
        url = reverse('farm:breed_patch', args=['1'])
        data = {
            'id': 1,
            'breed': 'very small chicken',
            'avg_eggs': 2,
            'avg_weight': 2,
            'diet': 'table 3'
        }
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)
        data['diet'] = 'table 6'
        response = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)


class ChickenPutTest(TestCase):

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

    def test_put_chicken(self):
        self.maxDiff = None
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
        data['egg_amount'], data['prev_eggs'] = 3, 2
        response = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)


class WorkingPatchTesst(TestCase):

    @classmethod
    def setUpTestData(cls):
        Cage.objects.create(shed=2,
                            row=5,
                            cage=23,
                            square=30)

        Cage.objects.create(shed=4,
                            row=1,
                            cage=13,
                            square=50)

        Worker.objects.create(name='Darya Kotelnikova',
                              passport='1111 330044',
                              position='vet',
                              salary=50000)

        Working.objects.create(name=Worker.objects.get(id=1),
                               cage=Cage.objects.get(id=1),
                               work_type='med',
                               work_date='2022-05-06',
                               work_status=False)

    def test_update_working(self):
        self.maxDiff = None
        url = reverse('farm:working_patch', args=['1'])
        data = {'id': 1,
                'name': 1,
                'cage': 1,
                'work_type': 'med',
                'work_date': '2022-05-06',
                'work_status': False,
                'details': None
                }
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)
        data['cage'] = 2
        response = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)

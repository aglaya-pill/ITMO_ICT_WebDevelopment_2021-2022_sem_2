from django.test import TestCase
from ..models import *


class BreedModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Breed.objects.create(breed='very small chicken',
                             avg_eggs=2,
                             avg_weight=2,
                             diet='table 3')

    def test_diet_label(self):
        breed_sample = Breed.objects.get(id=1)
        field_label = breed_sample._meta.get_field('diet').verbose_name
        self.assertEquals(field_label, 'Diet for this breed')


class WorkerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Worker.objects.create(name='Darya Kotelnikova',
                              passport='1111 330044',
                              position='vet',
                              salary=50000)

    def test_name_max_length(self):
        worker_sample = Worker.objects.get(id=1)
        max_length = worker_sample._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)


class ChickenModelTest(TestCase):

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

    def test_chicken_str_output(self):
        chicken_sample = Chicken.objects.get(id=1)
        expected_name = str(chicken_sample.breed) + ' ' + str(chicken_sample.cage)
        self.assertEquals(str(chicken_sample), expected_name)

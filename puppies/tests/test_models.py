from django.test import TestCase
from puppies.models import Puppy


class PuppyTest(TestCase):
    """
        Test puppy model
    """

    def setUp(self):
        Puppy.objects.create(
            name='Bambi', age='17', breed='puddle-cocker', color='Black')
        Puppy.objects.create(
            name='Phoebe', age='5', breed='golden retriever', color='Gold')

    def test_puppy_breed(self):
        puppy_bambi = Puppy.objects.get(name='Bambi')
        puppy_phoebe = Puppy.objects.get(name='Phoebe')
        self.assertEqual(
            puppy_bambi.get_breed(), "Bambi belongs to puddle-cocker breed.")
        self.assertEqual(
            puppy_phoebe.get_breed(),
            "Phoebe belongs to golden retriever breed.")

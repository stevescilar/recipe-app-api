from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """ check/ Test  that two numbers add up"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """ Test that two value subtract and return """
        self.assertEqual(subtract(5, 10), 5)
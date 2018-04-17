import unittest


class RomanNumeralsConverter:
    def __init__(self):
        self.transformations = {
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

    def from_int(self, number: int) -> str:
        roman_number = ''

        if number == 9:
            roman_number = self.transformations[9]
            number -= 9

        if number >= 5:
            roman_number = self.transformations[5]
            number -= 5

        if number == 4:
            roman_number = self.transformations[4]
            number -= 4

        while number >= 1:
            roman_number += self.transformations[1]
            number -= 1

        return roman_number


class RomanNumeralsTests(unittest.TestCase):

    def setUp(self):
        self.converter = RomanNumeralsConverter()

    def assertRomanNumeralFor(self, given_number, _is):
        result = self.converter.from_int(number=given_number)
        self.assertEqual(_is, result)

    def test_for_negative_numbers_returns_empty_string(self):
        self.assertRomanNumeralFor(given_number=-1, _is='')

    def test_for_zero_should_return_empty_string(self):
        self.assertRomanNumeralFor(given_number=0, _is='')

    def test_for_one_should_return_I(self):
        self.assertRomanNumeralFor(given_number=1, _is='I')

    def test_for_two_should_return_II(self):
        self.assertRomanNumeralFor(given_number=2, _is='II')

    def test_for_four_should_return_IV(self):
        self.assertRomanNumeralFor(given_number=4, _is='IV')

    def test_for_five_should_return_V(self):
        self.assertRomanNumeralFor(given_number=5, _is='V')

    def test_for_six_should_return_VI(self):
        self.assertRomanNumeralFor(given_number=6, _is='VI')

    def test_for_nine_should_return_IX(self):
        self.assertRomanNumeralFor(given_number=9, _is='IX')

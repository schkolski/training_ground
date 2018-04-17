import unittest


class RomanNumeralsConverter:
    def from_int(self, number):
        if number > 0:
            return 'I'
        else:
            return ''


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

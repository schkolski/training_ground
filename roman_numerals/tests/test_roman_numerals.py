import unittest


class RomanNumeralsConverter:
    def from_int(self, number):
        return ''


class RomanNumeralsTests(unittest.TestCase):

    def test_for_negative_numbers_returns_empty_string(self):
        converter = RomanNumeralsConverter()
        result = converter.from_int(number=-1)
        self.assertEqual('', result)

    def test_for_zero_should_return_empty_string(self):
        converter = RomanNumeralsConverter()
        result = converter.from_int(number=0)
        self.assertEqual('', result)

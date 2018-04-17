import unittest


class RomanNumeralsConverter:
    def __init__(self):
        self.transformations = {
            1000: 'M', 900: 'CM',
            500 : 'D', 400: 'CD',
            100 : 'C', 90 : 'XC',
            50  : 'L', 40 : 'XL',
            10  : 'X', 9  : 'IX',
            5   : 'V', 4  : 'IV',
            1   : 'I'
        }
        self.transformation_keys = list(reversed(sorted(self.transformations.keys())))

    def from_int(self, number: int) -> str:
        roman_number = ''

        for transformation_key in self.transformation_keys:
            while number >= transformation_key:
                roman_number += self.transformations[transformation_key]
                number -= transformation_key

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

    def test_for_ten_should_return_X(self):
        self.assertRomanNumeralFor(given_number=10, _is='X')

    def test_for_eleven_should_return_XI(self):
        self.assertRomanNumeralFor(given_number=11, _is='XI')

    def test_for_fourteen_should_return_XIV(self):
        self.assertRomanNumeralFor(given_number=14, _is='XIV')

    def test_for_fifteen_should_return_XV(self):
        self.assertRomanNumeralFor(given_number=15, _is='XV')

    def test_for_nineteen_should_return_XIX(self):
        self.assertRomanNumeralFor(given_number=19, _is='XIX')

    def test_for_twenty_should_return_XX(self):
        self.assertRomanNumeralFor(given_number=20, _is='XX')

    def test_for_forty_should_return_XL(self):
        self.assertRomanNumeralFor(given_number=40, _is='XL')

    def test_for_fifty_should_return_X(self):
        self.assertRomanNumeralFor(given_number=50, _is='L')

    def test_for_fifty_should_return_LX(self):
        self.assertRomanNumeralFor(given_number=60, _is='LX')

    def test_for_100_should_return_C(self):
        self.assertRomanNumeralFor(given_number=100, _is='C')

    def test_for_90_should_return_XC(self):
        self.assertRomanNumeralFor(given_number=90, _is='XC')

    def test_for_500_should_return_D(self):
        self.assertRomanNumeralFor(given_number=500, _is='D')

    def test_for_400_should_return_CD(self):
        self.assertRomanNumeralFor(given_number=400, _is='CD')

    def test_for_600_should_return_DC(self):
        self.assertRomanNumeralFor(given_number=600, _is='DC')

    def test_for_1000_should_return_M(self):
        self.assertRomanNumeralFor(given_number=1000, _is='M')

    def test_for_900_should_return_CM(self):
        self.assertRomanNumeralFor(given_number=900, _is='CM')

    def test_for_1100_should_return_MC(self):
        self.assertRomanNumeralFor(given_number=1100, _is='MC')

    def test_integration_tests(self):
        self.assertRomanNumeralFor(given_number=982,  _is='CMLXXXII')
        self.assertRomanNumeralFor(given_number=1991, _is='MCMXCI')
        self.assertRomanNumeralFor(given_number=1658, _is='MDCLVIII')
        self.assertRomanNumeralFor(given_number=1659, _is='MDCLIX')
        self.assertRomanNumeralFor(given_number=2018, _is='MMXVIII')
        self.assertRomanNumeralFor(given_number=4999, _is='MMMMCMXCIX')

class RomanNumeralsConverter:
    def __init__(self):
        self.transformations = {
            1000: 'M', 900: 'CM',
            500: 'D', 400: 'CD',
            100: 'C', 90: 'XC',
            50: 'L', 40: 'XL',
            10: 'X', 9: 'IX',
            5: 'V', 4: 'IV',
            1: 'I'
        }
        self.transformation_keys = list(reversed(sorted(self.transformations.keys())))

    def from_int(self, number: int) -> str:

        roman_number_transformations = list()
        for transformation_key in self.transformation_keys:
            if number >= transformation_key:
                roman_number_transformations.append(
                    self.transform(number, transformation_key))
                number %= transformation_key

        return ''.join(roman_number_transformations)

    def transform(self, number, transformation_key):
        reps = number // transformation_key
        return self.transformations[transformation_key] * reps
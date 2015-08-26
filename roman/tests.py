from django.test import TestCase

from views import convert_to_roman


class RomanConvertTests(TestCase):

    def test_decimal_to_roman(self):
        self.assertEqual(convert_to_roman(6), 'VI')
        self.assertEqual(convert_to_roman(18), 'XVIII')
        self.assertEqual(convert_to_roman(19), 'XIX')
        self.assertEqual(convert_to_roman(38), 'XXXVIII')
        self.assertEqual(convert_to_roman(39), 'XXXIX')
        self.assertEqual(convert_to_roman(40), 'XL')
        self.assertEqual(convert_to_roman(98), 'XCVIII')
        self.assertEqual(convert_to_roman(388), 'CCCLXXXVIII')
        self.assertEqual(convert_to_roman(499), 'CDXCIX')
        self.assertEqual(convert_to_roman(867), 'DCCCLXVII')
        self.assertEqual(convert_to_roman(1998), 'MCMXCVIII')
        
    def test_boundary_decimal_to_roman(self):
        self.assertEqual(convert_to_roman(1), 'I')
	self.assertEqual(convert_to_roman(3999), 'MMMCMXCIX')

    def test_speical_input_decimal_to_roman(self):
        self.assertEqual(convert_to_roman(001), 'I')
	self.assertEqual(convert_to_roman(0002), 'II')



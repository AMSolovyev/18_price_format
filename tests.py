from format_price import get_formatted_price
import unittest


class TestGetFormatPrice(unittest.TestCase):
    def test_check_digit_to_be_equal(self):
        price = 12.0000
        self.assertEqual(get_formatted_price(price), '12')

    def test_check_digit_to_be_None(self):
        price = 12, 000
        self.assertIsNone(get_formatted_price(price))

    def test_check_digit_True(self):
        price = 12000
        self.assertTrue(get_formatted_price(price))

    def test_check_digit_True2(self):
        price = 12000
        self.assertEqual(get_formatted_price(price), '12 000')

    def test_check_negative(self):
        price = - 12.00
        self.assertEqual(get_formatted_price(price), '-12')

    def test_check_empty(self):
        price = ''
        self.assertIsNone(get_formatted_price(price))
        price = None
        self.assertIsNone(get_formatted_price(price))

    def test_check_string(self):
        price = 'fgh356'
        self.assertIsNone(get_formatted_price(price))

    def test_cheks_zero(self):
        price = 0
        self.assertEqual(get_formatted_price(price), '0')

    def test_check_list(self):
        price = [12, 56.97, 35.00]
        self.assertIsNone(get_formatted_price(price))

    def test_check_tuple(self):
        price = (23.09, 56.09, -78.00)
        self.assertIsNone(get_formatted_price(price))

    def test_check_dict(self):
        price = {'milk': 23.09, 'tomato': 56.09, 'pear': 78.056}
        self.assertIsNone(get_formatted_price(price))

    def test_check_set(self):
        price = {'car', 32.09, 'book', 45.008}
        self.assertIsNone(get_formatted_price(price))


if __name__ == '__main__':
    unittest.main()

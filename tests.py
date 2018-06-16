from format_price import get_format_price
import unittest


class TestGetFormatPrice(unittest.TestCase):
    def test_check_digits(self):
        price = 12.0000
        self.assertEqual(get_format_price(price), 12)
        price = 12, 000
        self.assertIsNone(get_format_price(price), 12000)
        price = 12000
        self.assertIsNotNone(get_format_price(price))

    def test_check_negative(self):
        price = - 12.00
        self.assertTrue(get_format_price(price))

    def test_check_empty(self):
        price = ''
        self.assertIsNone(get_format_price(price))

    def test_check_string(self):
        price = 'fgh356'
        self.assertIsNone(get_format_price(price))

    def test_cheks_zero(self):
        price = 0
        self.assertIsNotNone(get_format_price(price), 0)


if __name__ == '__main__':
    unittest.main()

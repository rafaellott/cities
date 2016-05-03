from src.cities import Cities
import unittest


class TestCities(unittest.TestCase):
    def setUp(self):
        self.cities = Cities()

    def test_raise_convert_dms_to_decimal(self):
        self.assertRaises(
            ValueError,
            self.cities.dms_to_decimal,
            lat_degrees="53 20 19",
            long_degrees="6 15 37 W"
        )
        self.assertRaises(
            ValueError,
            self.cities.dms_to_decimal,
            lat_degrees="53 20 19 N",
            long_degrees="6 15"
        )

    def test_only_int_numbers(self):
        self.assertRaises(
            Exception,
            self.cities.dms_to_decimal,
            lat_degrees="53 20 19 N",
            long_degrees="6 15 2.4 W"
        )

    def test_right_numbers(self):
        self.assertEquals(
            self.cities.dms_to_decimal(
                lat_degrees="53 20 19 N",
                long_degrees="6 15 37 W"
            ),
            [53.3498, 6.2603]
        )

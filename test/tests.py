from src.cities import Cities
import unittest


class TestCities(unittest.TestCase):
    def setUp(self):
        self.cities = Cities()

    def test_raise_convert_dms_to_decimal(self):
        self.assertRaises(
            ValueError,
            self.cities.dms_to_decimal,
            lat_degrees="53d 20m 19s",
            long_degrees="6d 15m 37s W"
        )
        self.assertRaises(
            ValueError,
            self.cities.dms_to_decimal,
            lat_degrees="53d 20m 19s N",
            long_degrees="6d 15m W"
        )

# coding=UTF-8
'''File containing the application's souce code.'''
import json
import os
import sys
from math import radians, cos, sin, asin, sqrt


class Cities(object):

    def __init__(
        self,
        origin_city=[53.3497, -6.2603],
        city_file='cities.json',
        max_distance=500,
    ):
        if city_file[0] is not '/':
            BASE_DIR = os.path.dirname(__file__)
            if not BASE_DIR:
                BASE_DIR = (
                    os.path.dirname(
                        os.path.abspath(sys.modules['__main__'].__file__))
                )
            city_file = BASE_DIR + '/' + city_file
        self.origin_city = origin_city
        self.city_file = city_file
        self.max_distance = max_distance
        self.earth_radius = 6371

    def dms_to_decimal(self, lat_degrees, long_degrees):
        '''
        Convert Degree/Minute/Second to Decimal.

        If one of DMS is 0, send it 0 [53d 0m 0s N]
        params:
            degree / minute / second / location North, South, West or East
            string "53 20 19 N"
            string "6 15 37 W"
        return:
            arrays of float
            53.3498
            -6.2603
        '''
        lat_split = lat_degrees.split(' ')
        long_split = long_degrees.split(' ')
        if len(lat_split) is not 4:
            raise ValueError("Invalid latitude value")
        if len(long_split) is not 4:
            raise ValueError("Invalid longitude value")
        lat_dec = 0
        long_dec = 0
        try:
            lat_dec = round(
                float(
                    float(lat_split[0]) +
                    float(lat_split[1])/60 +
                    float(lat_split[2])/3600
                ),
                4
            )
            long_dec = round(
                float(
                    float(long_split[0]) +
                    float(long_split[1])/60 +
                    float(long_split[2])/3600
                ),
                4
            )
            if lat_split[-1].upper() == 'S':
                lat_dec = -lat_dec
            if long_split[-1].upper() == 'W':
                long_dec = -long_dec
            return [lat_dec, long_dec]
        except Exception as e:
            raise Exception(str(e) + "\nInvalid number for latitude/longitude")

    def read_json_file(self):
        '''Read a json file and return it as dict.'''
        with open(self.city_file) as data_file:
            return json.load(data_file)

    def distance_from_threhold(self, coordinates):
        '''
        calculate the great circle distance between two points
        on the Earth (coordinates specified in decimal degrees)
        '''
        # convert decimal degrees to radians
        lat1, lon1, lat2, lon2 = map(
            radians,
            [
                self.origin_city[0], self.origin_city[1],
                coordinates[0], coordinates[1]
            ]
        )

        # Haversine formula
        dif_lon = lon2 - lon1
        dif_lat = lat2 - lat1
        a = sin(dif_lat/2)**2 + cos(lat1) * cos(lat2) * sin(dif_lon/2)**2
        c = 2 * asin(sqrt(a))

        return True if round(6367 * c, 1) <= self.max_distance else False

    def calculate_cities(self):
        cities = self.read_json_file()
        close_cities = []
        for city, points in cities.iteritems():
            if self.distance_from_threhold(
                coordinates=[points.get('lat'), points.get('lon')]
            ):
                close_cities.append(city)
        return sorted(close_cities)

    def start(self):
        text = (
            "Cities in %skm range of Dublin" % self.max_distance
        )
        cities = self.calculate_cities()
        text += ("There are %s cities near Dublin" % len(cities))
        for city in cities:
            text += (city.title())
        return text

if __name__ == "__main__":
    cities_obj = Cities()
    print(cities_obj.start())

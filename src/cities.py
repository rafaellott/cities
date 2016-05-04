# coding=UTF-8
'''File containing the application's souce code.'''
import json
import os
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

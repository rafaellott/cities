# coding=UTF-8
'''File containing the application's souce code.'''


class Cities(object):

    def __init__(self):
        pass

    def dms_to_decimal(self, lat_degrees, long_degrees):
        '''
        Convert Degree/Minute/Second to Decimal
        If one of DMS is 0, send it 0 [53d 0m 0s N]
        params:
            d -> degree / m -> minute / s-> second
            string "53d 20m 19s N"
            string "6d 15m 37s W"
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
        # Decimal Degrees = Degrees + minutes/60 + seconds/3600

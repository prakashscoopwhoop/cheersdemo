
import math
import logging
import pdb
import sys
from decimal import Decimal, getcontext

x = 2.31


class MathMethod:
    '''
    Use for defining maths functions.
    '''

    def get_sin(self, radian):
        '''
        :param radian:
        '''
        return math.sin(radian)

    def get_cos(self, radian):
        '''
        :param radian:
        '''
        return math.cos(radian)

    def get_pi(self):
        '''
        Bailey–Borwein–Plouffe formula
        '''
        getcontext().prec = 100
        pi = sum(1 / Decimal(16)**k *
                 (Decimal(4) / (8 * k + 1) -
                  Decimal(2) / (8 * k + 4) -
                  Decimal(1) / (8 * k + 5) -
                  Decimal(1) / (8 * k + 6)) for k in range(100))

        return round(pi, 4)

    def convert_degree_radian(self, degree):
        '''
        :param degree:
        '''
        return math.radians(degree)

    def convert_radian_degree(self, radian):
        '''
        :param radian:
        '''
        return math.degrees(radian)


class Incarnation2:
    '''
    For finding alpha and length of segment of coasters.
    '''
    _math_method = MathMethod()

    def find_alpha(self):
        '''
        x - sinx = pi/2
        - sinx = pi/2 -x
        sinx = -(pi/2-x)
        sin(sinx) = sin(-(pi/2 -x))     ( sin(-x) = -sinx)
        sin(sinx) = -sin(pi/2 -x)
        sin(sinx) + sin(pi/2 -x)
        sin(sinx) + cos(x) = 0         ( sin(90 - x) = cos x)

        '''
        sin_value = self._math_method.get_sin(self._math_method.get_sin(x))
        cos_value = self._math_method.get_cos(x)

        if round(sin_value, 2) + round(cos_value, 2) == 0:
            print("Alpha: " + str(x))
            return x
        else:
            print("x is not an alpha")
            return

    def get_length_of_segment(self, r_value):
        '''
        r_value radius of coasters
        '''
        try:
            if '--debugger' in sys.argv:
                pdb.set_trace()
            alpha = self.find_alpha()
            cos_value = self._math_method.get_cos(alpha / 2)
            length = 2 * r_value * (1 - cos_value)
            return length
        except Exception as ex:
            logging.error(ex)
            return


if __name__ == "__main__":

    # Logger
    logging.basicConfig(
        filename='cheers.log',
        level=logging.INFO,
        format='%(asctime)s: %(name)-4s: %(levelname)-4s: %(message)s',
        datefmt='%Y-%m-%d %Hh %Mm %Ss')

    logging.info("start the process")

    while True:
        try:
            radius = input("Please enter the value of radius: ")
            seg_length = round(Incarnation2().get_length_of_segment(float(radius)), 2)
            print(
                "length of segment of coasters: " +
                str(seg_length) +
                " whose radius " +
                str(radius))
        except Exception as ex:
            print("please enter the valid input")

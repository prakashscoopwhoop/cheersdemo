
import math
import logging
import argparse

x = 2.31

def get_sin(r):
    return math.sin(r)


def get_cos(r):
    return math.cos(r)


def get_pi():
    return math.pi
 
    
def convert_degree_radian(d):
    return math.radians(d)


def convert_radian_degree(r):
    return math.degrees(r)


def find_alpha():
    '''
    x - sinx = pi/2
    - sinx = pi/2 -x
    sinx = -(pi/2-x)
    sin(sinx) = sin(-(pi/2 -x))     ( sin(-x) = -sinx)
    sin(sinx) = -sin(pi/2 -x)
    sin(sinx) + sin(pi/2 -x)
    sin(sinx) + cos(x) = 0         ( sin(90 - x) = cos x)
    
    '''
    sin_value = get_sin(get_sin(x))
    cos_value = get_cos(x)
  
    if round(sin_value,2) + round(cos_value,2) == 0:
        print("Alpha: "+ str(x))
        return x
    else:
        print("x is not an alpha")
        return


def get_length_of_segment(R):
    '''
    R radius of coasters
    '''
    try:
        alpha = find_alpha()
        cos_value = get_cos(alpha/2)
        l = 2*R * (1 - cos_value)
        return l
    except Exception as e:
        print(e)
        return 
        


if __name__ == "__main__":
    
    # Logger
    logging.basicConfig(filename='cheers.log',
                        level=logging.INFO,
                        format='%(asctime)s: %(name)-4s: %(levelname)-4s: %(message)s',
                        datefmt='%Y-%m-%d %Hh %Mm %Ss')
    
    logging.info("start the process")
    try:
        r = input("Please enter the value of redius: ")    
        l = round(get_length_of_segment(float(r)),2)
        print(l)
        print("length of segment of coasters: "+str(l)+ " whose radius "+ str(r))
    except Exception as e:
            print("please enter the value input")
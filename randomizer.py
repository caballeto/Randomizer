"""
    Pseudo randomizer with simple approach.
"""

import time
import math
import sys

from tqdm import tqdm
from math import pi, e

GOLD = 1.618033
FILE_OUT = 'dataset.csv'

class Randomizer(object):
    def __init__(self):
        self.amplitude = 32767
        self.i = 1
        self.x = float(hash(str(time.time()))) % 15487271

    def r1(self, x):
        return self.amplitude*math.sin(10000*self.r2(x))

    def r2(self, y):
        return self.amplitude*math.sin(20*y)

    def random(self):
        res = self.r1(self.x)
        self.i += 1

        # adding some random behaviour
        if self.i%2 == 0: self.x += 1.19*math.sqrt(e/pi)
        if self.i%3 == 0: self.x += 2.08*math.sqrt(e/pi) + math.sqrt(e)
        if self.i%7 == 0: self.x += 13.44*(pi/e)
        if self.i%10 == 0: self.x += 3.12*pi*e
        if self.i%13 == 0: self.x += 7.74*e*GOLD
        if self.i%19 == 0: self.x += 4.65*e**2
        if self.i%23 == 0: self.x += self.r1(pi);

        # check overflow
        if(self.x > 15487271):
            self.x = self.x/(pi**10)

        if(self.i > 10000):
            self.i = math.floor(self.i/(e**11))

        # add changes
        self.x += self.i*pi/5000 + GOLD*self.i/(e**4)

        return int(math.floor(res))

def main():
    randomizer = Randomizer()

    with open(FILE_OUT, 'w') as file:
        file.write(str(0) + ',' + 'random')

        for i in tqdm(range(1, 1000000)):
            file.write(str(i) + ',' + str(randomizer.random()) + '\n')

if __name__ == '__main__':
    main()

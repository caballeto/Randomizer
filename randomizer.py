"""
    Fake randomizer simple approach.
"""
import math
import sys

class Randomizer(object):
    def __init__(self):
        self.pi = math.pi
        self.e = math.e
        self.gold = 1.618033
        self.amplitude = 32767
        self.i = 0
	self.i = 1001 # warning here the tab may not work as it is for you, depends how much spaces in tab you have. Correct save fn so.
	self.x = float(26217.4511684)
    def r1(self, x):
        return self.amplitude*math.sin(10000*self.r2(x))

    def r2(self, y):
        return self.amplitude*math.sin(20*y)

    def save(self, x, i):
        with open('randomizer.py', 'r') as file:
            data = file.readlines()
        data[15] = ('\t' + 'self.x = ' + 'float(' + str(x) + ')' + '\n')
        data[14] = ('\t' + 'self.i = ' + str(i) + '\n')

        with open('randomizer.py', 'w') as file:
            file.writelines(data)

    def random(self):
        res = self.r1(self.x)
        self.i += 1

        # adding some random behaviour
        if self.i%2 == 0: self.x += 1.19*math.sqrt(self.e/self.pi)
        if self.i%3 == 0: self.x += 2.08*math.sqrt(self.e/self.pi) + math.sqrt(self.e)
        if self.i%7 == 0: self.x += 13.44*(self.pi/self.e)
        if self.i%10 == 0: self.x += 3.12*self.pi*self.e
        if self.i%13 == 0: self.x += 7.74*self.e*self.gold
        if self.i%19 == 0: self.x += 4.65*self.e**2
        if self.i%23 == 0: self.x += self.r1(self.pi);

        # check overflow
        if(self.x > 10000000):
            self.x = self.x/(self.pi**10)

        if(self.i > 10000):
            self.i = math.floor(self.i/(self.e**11))

        # add changes
        self.x += self.i*self.pi/5000 + self.gold*self.i/(self.e**4)

        # save result
        self.save(self.x, self.i)
        return int(math.floor(res))

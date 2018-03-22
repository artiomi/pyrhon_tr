import random
random.random()

random.choice([1, 2, 3, 4])
name = 'Artiom'
dir(name)
help(name.zfill)

import struct
packed = struct.pack('>i4sh', 7, b'spam', 8)
packed

file = open('data.bin', 'wb')
file.write(packed)
file.close()
file = open('data.bin', 'r')
print(file.read())

from fractions import Fraction
 x = Fraction(3, 3)
 y = Fraction(4, 6)
 
 import sys
 sys.getrefcount(1000)
 
 S = 'abcedfg'
S[-1:]

ord('o')
chr(112)

 L = ['abc', 'ABD', 'aBe']
 sorted(L, key=str.lower, reverse=True)
 
 D = {'spam': 2, 'ham': 1, 'eggs': 3}
 
 from collections import namedtuple
 Rec = namedtuple('Rec', ['name', 'age', 'jobs'])
  bob = Rec('Bob', age=40.5, jobs=['dev', 'mgr'])
O = bob._asdict()

myfile = open('myfile.txt', 'w')
 myfile.write('hello text file\n')
myfile.write('goodbye text file\n')
myfile.close()

myfile = open('myfile.txt')
myfile.readlines()
myfile.readline()
print('90')

L = [None] * 100
dir(L)
len(L)
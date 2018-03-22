class Number:
    
    def __init__(self, start):
        self.data = start
    
    def __sub__(self, other):
        return Number(self.data + other)

X= Number(5)
y= X - 2
y.data

class Exitloop(Exception): pass

try:
    while True:
        while True:
            for i in range(10):
                if i > 3: raise Exitloop
                print('loop3: %s' % i)
            print('loop2')
        print('loop1')
except Exitloop:
    print('continuing')
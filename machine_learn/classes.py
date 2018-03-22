class FirstClass:
    
    def setdata(self, value):
        self.data = value
        
    def display(self):
        print(self.data)

x = FirstClass()
y = FirstClass()

class SecondClass(FirstClass):
    
    def hello(self):
        print("hi")


        
class ThirdClass(SecondClass):
    
    def __init__(self, value):
        self.data = value
        
    def __add__(self, other):
        return ThirdClass(self.data + other)
    
    def __str__(self):
        return '[ThirdClass: %s]' % self.data
    
    def mul(self, other):
        self.data *= other


#class SecondParentClass:
#    
#    def setdata(self, value):
#        self.attr = value
#        
#    def display(self):
#        print('Third class attr = "%s"' % self.attr)
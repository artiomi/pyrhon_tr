X=10

def times(x, y):
    global X
    X = 2
    print(X)
    return x * y

print(X)

times(2,3)
period=times
period(3,4)
############
X = 99 
def f1():
    X = 88 
    def f2():
        print(X) 
    f2()
f1()
###########3
def func(spam, eggs, toast=0, ham=0):
    print((spam, eggs, toast, ham))
    
func(1, spam=3, eggs=0)
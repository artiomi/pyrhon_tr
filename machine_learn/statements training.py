if True :
    print("Hello ")
    print("Artiom")
else : print("No")

while True:
    a = input('Enter text:')
    if a == 's': break
    print(a.upper())
print("Bye")

*a, b = 'spma'

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a,b,c)
    
if 1:
    x=(1+2+3
       +4)
    print(x)
    
S = ('aaaa'
'bbbb' # Comments here are ignored
'cccc')

X=1

if X == "hi":
    print("ok")
else:
    print("KO")

S = 'spam'
for i in range(len(S)):
    S = S[1:] + S[:1] 
    print(S, end=' ')
    
import os
for line in os.popen('systeminfo'): print(line.rstrip())
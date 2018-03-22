if True:
   print("Answer")
   print( "True")
else:
   print("Answer")
   print("False")
   
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']


print(list)    # Prints complete list
print( list[0]    )   # Prints first element of the list
print( list[1:3]  )   # Prints elements starting from 2nd till 3rd 
print( list[2:]   )   # Prints elements starting from 3rd element
print( tinylist * 2 ) # Prints list two times
print( list + tinylist) # Prints concatenated lists

a=10
id(a)
id(10)

i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j):
          print("break on",i,j)
          break
      j = j + 1
   if (j > i/j) : print( i, " is prime")
   i = i + 1

print( "Good bye!")
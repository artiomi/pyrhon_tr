#first
my_list =[0,1,2,3,4,5,6,7]

import numpy as np
arr = np.array(my_list)

arr2= np.arange(0,10,3)

lin_sp = np.linspace(0,1,20)

ranarr = np.random.randint(0,50, 10)

arr2.reshape(2,2)
arr2.dtype

# second
arr = np.arange(0,11)

arr_2d = np.array([[5,6,7],[8,9,10],[11,12,13]])

arr_2d[1:,:-1]

bool_arr = arr>5

arr[bool_arr]

arr_2d_2 = np.arange(50).reshape(5,10)

arr_2d_2[3:5,2:4]

arr = np.arange(0,11).reshape(2,2)
arr.sum()
help(arr.sum)


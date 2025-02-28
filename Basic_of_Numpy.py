import numpy as np
arr = np.array([[1,2,3],[2,3,4]])
print(arr[0:1])

import numpy as np
arr = np.array([[1,2,3],[2,3,4]])
print(arr[::-1])

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])
newarr=arr.reshape(3,3)
print(newarr)

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(3,4)
print(newarr)

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(2,3,2) #2 row 3col 2 elem
print(newarr)

#Bulitin function
import numpy
dir(numpy)

import numpy as np
arr1=np.array([[1,2],[4,5]])
arr2=np.array([[5,6],[5,7]])
result=np.concatenate((arr1,arr2),axis=0)
print(result)

import numpy as np
arr1=np.array([1,2,3,4,5,6,7,8,9,10])
new_arr=np.array_split(arr1, 3)
print(new_arr)


#Search arr
import numpy as np
arr1=np.array([1,2,3,4,5,6,7,8,9,10])
x=np.where(arr1==10)
print(x)


#check even number in element
import numpy as np
arr1=np.array([1,2,3,4,5,6,7,8,9,10])
x=np.where(arr1&2==0)
print(x)


#Sorting
import numpy as np
arr=np.array([6,3,7,1,4])
x=np.sort(arr)
print(x)



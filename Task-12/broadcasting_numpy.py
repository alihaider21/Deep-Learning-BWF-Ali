#Topics: Broadcasting in Numpy Array

import numpy as np

#Add a scalar to a 2D array
a = np.array([[1, 2, 3], [4, 5, 6]])
b = 2
c = a + b
print("Add a scalar to a 2D array: \n",c)


#Subtract a 1D array from a 2D array
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([1, 2, 3])
c = a - b
print("Subtract a 1D array from a 2D array: \n",c)


#Divide a 2D array by a scalar
a = np.array([[1, 2, 3], [4, 5, 6]])
b = 2
c = a / b
print("Divide a 2D array by a scalar: \n",c)


#importing libraries
import numpy as np

#intalizing 1-D array
arr = np.array([1, 2, 3, 4, 5])
print("1D Numpy Array \n",arr)

#intalizing 2-D array
arr_2d = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]])
print("2D Numpy Array \n",arr_2d)

# two multi-dimensional NumPy arrays of the same shape
arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2 = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

#Addition
print("Addition \n",arr1 + arr2)

#Subtraction
print("Subtraction \n",arr1 - arr2)

#Multiplication
print("Multiplication \n",arr1 * arr2)

#Division
print("Division \n",arr1 / arr2)
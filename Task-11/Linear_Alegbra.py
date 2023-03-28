#Linear Algebra with Numpy:
import numpy as np

#Create a 3x3 matrix using numpy and print it.
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("3x3 Numpy Matrix \n",array)


#Create a 3x3 identity matrix using numpy and print it.
identity_array = np.identity(5)
print("Identity 5x5 Matrix \n",identity_array)

#Create a 3x3 matrix with random values using numpy and print it.
random_array = np.random.randint(10,size=(3,3))
print("Random Value 3x3 Matrix \n",random_array)

#Create a 3x3 matrix with ones on the diagonal and zeros everywhere else using numpy and print it.
eye_array = np.eye(3)
print("3x3 Matrix ones on the diagonal \n",eye_array )

#Create two 3x3 matrices with random values and calculate their dot product using numpy.
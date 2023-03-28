#Statistical Functions with Numpy
import numpy as np

#Create an array of 10 random integers between 1 and 100 using numpy.
array = np.random.randint(100, size=(10))
print("Array of 10 random\n",array)

#Calculate the mean of the array using numpy.
print("Mean of the Array:",np.mean(array))

#Calculate the Median of the array using numpy.
print("Median of the Array:",np.std(array))

#Calculate the standard deviation  of the array using numpy.
print("Standard Deviation of the Array:",np.std(array))

#Create another array of 10 random integers between 1 and 100 using numpy and calculate the correlation coefficient between the two arrays using numpy.
array_1 = np.random.randint(100, size=(10))
print("Correlation coefficient between the two arrays:",np.corrcoef(array,array_1))

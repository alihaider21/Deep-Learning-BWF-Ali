#There are several ways to check the execution time of your code 
#In this exercise i will use 2 diffrent ways to check the execution time of your code

#Example 1: Using time.time()
import time

start_time = time.time()

# Your code here

end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")


#Example 2: Using timeit
import timeit

code_to_test = """
# Your code here
"""

execution_time = timeit.timeit(code_to_test, number=1)

print(f"Execution time: {execution_time} seconds")

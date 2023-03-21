#There are several ways to check the execution time of your code 
#In this exercise i will use time.time to check the execution time of your code

#Example 1: Using time.time()
import time

start_time = time.time()

# Your code here
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)


end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")


#Example 2: Using time.time()
import time
start_time = time.time()

age = 35

if age < 2:
    print("This person is a baby.")
elif age < 4:
    print("This person is a toddler.")
elif age < 13:
    print("This person is a kid.")
elif age < 20:
    print("This person is a teenager.")
elif age < 65:
    print("This person is an adult.")
else:
    print("This person is an elder.")

end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")

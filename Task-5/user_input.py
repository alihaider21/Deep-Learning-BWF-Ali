#7-1. Rental Car: 

car_type = input("What kind of rental car would you like? ")
print("Let me see if I can find you a " + car_type + ".")

#7-2. Restaurant Seating: 

group_size = int(input("How many people are in your dinner group? "))
if group_size > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")


#7-3. Multiples of Ten:
number = int(input("Please enter a number: "))
if number % 10 == 0:
    print(number, "is a multiple of 10.")
else:
    print(number, "is not a multiple of 10.")



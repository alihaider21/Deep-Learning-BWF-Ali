#5-1. Conditional Tests

# variables
age = 21
name = 'Ali'
height_cm = 180
weight_kg = 60.5
is_student = True

# Test 1: Check if age is greater than 18
print("Is age greater than 18? I predict True.")
print(age > 18)

# Test 2: Check if name is 'Ali'
print("Is name 'Ali'? I predict True.")
print(name == 'Ali')

# Test 3: Check if height is less than 170 cm
print("Is height less than 170 cm? I predict True.")
print(height_cm < 190)

# Test 4: Check if weight is between 60 kg and 70 kg
print("Is weight between 60 kg and 70 kg? I predict True.")
print(60 < weight_kg < 70)

# Test 5: Check if name is not 'Bob'
print("Is name not 'Bob'? I predict True.")
print(name != 'Bob')

# Test 6: Check if age is less than or equal to 20
print("Is age less than or equal to 20? I predict False.")
print(age <= 20)

# Test 7: Check if is_student is False
print("Is is_student False? I predict False.")
print(is_student == False)

# Test 8: Check if weight is greater than 70 kg
print("Is weight greater than 70 kg? I predict False.")
print(weight_kg > 70)

# Test 9: Check if name is 'Ali' (uppercase)
print("Is name 'Ali' (uppercase)? I predict False.")
print(name == 'Ali')

# Test 10: Check if age is a string
print("Is age a string? I predict False.")
print(isinstance(age, str))



#5-2. More Conditional Tests

# Equality and inequality tests with strings
name = 'Ali'
print("Is name equal to 'Ali'? I predict True.")
print(name == 'Ali')
print("Is name not equal to 'Haider'? I predict True.")
print(name != 'Haider')
print("Is name equal to 'ALI' (uppercase)? I predict False.")
print(name == 'ALI')
print("Is name not equal to 'ali' (lowercase)? I predict True.")
print(name != 'ali')

# Tests using the lower() function
fruit = 'APPLE'
print("Is fruit equal to 'apple' (lowercase)? I predict True.")
print(fruit.lower() == 'apple')
print("Is fruit not equal to 'orange'? I predict True.")
print(fruit.lower() != 'orange')
print("Is fruit equal to 'orange'? I predict False.")
print(fruit.lower() == 'orange')
print("Is fruit not equal to 'apple'? I predict False.")
print(fruit.lower() != 'apple')

# Numerical tests
age = 25
print("Is age equal to 25? I predict True.")
print(age == 25)
print("Is age not equal to 30? I predict True.")
print(age != 30)
print("Is age greater than 20? I predict True.")
print(age > 20)
print("Is age less than 30? I predict True.")
print(age < 30)
print("Is age greater than or equal to 25? I predict True.")
print(age >= 25)
print("Is age less than or equal to 25? I predict True.")
print(age <= 25)

# Tests using the and keyword and the or keyword
is_student = True
is_female = False
print("Is the person a female student? I predict False.")
print(is_student and is_female)
print("Is the person a student or female? I predict True.")
print(is_student or is_female)
print("Is the person not a student or not female? I predict False.")
print(not is_student or not is_female)
print("Is the person a student and not female? I predict True.")
print(is_student and not is_female)

# Tests for list membership
fruits = ['apple', 'banana', 'orange']
print("Is 'apple' in the list of fruits? I predict True.")
print('apple' in fruits)
print("Is 'kiwi' not in the list of fruits? I predict True.")
print('kiwi' not in fruits)
print("Is 'banana' not in the list of fruits? I predict False.")
print('banana' not in fruits)
print("Is 'orange' in the list of fruits? I predict True.")
print('orange' in fruits)


#5-5. Alien Colors #3


# Version 1: Green Alien
alien_color = 'green'

if alien_color == 'green':
    print("Congratulations, you earned 5 points!")
elif alien_color == 'yellow':
    print("Congratulations, you earned 10 points!")
else:
    print("Congratulations, you earned 15 points!")

# Version 2: Yellow Alien
alien_color = 'yellow'

if alien_color == 'green':
    print("Congratulations, you earned 5 points!")
elif alien_color == 'yellow':
    print("Congratulations, you earned 10 points!")
else:
    print("Congratulations, you earned 15 points!")

# Version 3: Red Alien
alien_color = 'red'

if alien_color == 'green':
    print("Congratulations, you earned 5 points!")
elif alien_color == 'yellow':
    print("Congratulations, you earned 10 points!")
else:
    print("Congratulations, you earned 15 points!")


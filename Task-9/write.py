#10-6. Addition

while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        break
    except ValueError:
        print("Error: Please enter a valid integer.")

try:
    result = num1 + num2
    print("The sum of", num1, "and", num2, "is", result)
except TypeError:
    print("Error: Please enter valid numbers.")

#10-7. Addition Calculator:

while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 + num2
        print("The sum of", num1, "and", num2, "is", result)
    except ValueError:
        print("Error: Please enter valid numbers.")
    except TypeError:
        print("Error: Please enter valid numbers.")
    else:
        choice = input("Would you like to add two more numbers? (y/n): ")
        if choice.lower() == "n":
            break


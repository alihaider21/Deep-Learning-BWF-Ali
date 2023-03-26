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

#10-8. Cats and Dogs:

try:
    # read the contents of cats.txt file
    with open('cats.txt', 'r') as cats_file:
        cats = cats_file.read()
        print("Contents of cats.txt:\n", cats)

    # read the contents of dogs.txt file
    with open('dogs.txt', 'r') as dogs_file:
        dogs = dogs_file.read()
        print("Contents of dogs.txt:\n", dogs)

except FileNotFoundError as e:
    print("File not found:", e.filename)


# create the cats.txt file
with open('cats.txt', 'w') as cats_file:
    cats_file.write("Fluffy\n")
    cats_file.write("Mittens\n")
    cats_file.write("Whiskers\n")

# create the dogs.txt file
with open('dogs.txt', 'w') as dogs_file:
    dogs_file.write("Buddy\n")
    dogs_file.write("Max\n")
    dogs_file.write("Charlie\n")

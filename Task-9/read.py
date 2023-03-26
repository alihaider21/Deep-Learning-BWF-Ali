#10-1. Learning Python: 
filename = "learning_python.txt"

# Read the entire file
with open(filename, "r") as f:
    contents = f.read()
    print(contents)
    print()

# Loop over the file object
with open(filename, "r") as f:
    for line in f:
        print(line, end="")
    print()

# Store the lines in a list and work with them outside the with block
with open(filename, "r") as f:
    lines = f.readlines()

for line in lines:
    print(line, end="")

#10-2. Learning C:
filename = 'learning_python.txt'
new_language = 'C'

with open(filename) as file_object:
    for line in file_object:
        modified_line = line.replace('Python', new_language)
        print(modified_line.strip())

#10-3. Guest:
filename = 'guest.txt'

# Prompt the user for their name
name = input("What is your name? ")

# Write the user's name to the file
with open(filename, 'w') as file_object:
    file_object.write(name)
    print("Your name has been written to the file.")


#10-4. Guest Book
filename = 'guest.txt'

# Prompt the user for their name
name = input("What is your name? ")

# Write the user's name to the file
with open(filename, 'w') as file_object:
    file_object.write(name)
    print("Your name has been written to the file.")


#10-4. Guest Book: 
filename = 'guest_book.txt'

while True:
    name = input("What is your name? (Enter 'q' to quit) ")
    
    if name == 'q':
        break
    
    # Print a greeting to the screen
    print(f"Welcome, {name}!")
    
    # Write the user's name to the file
    with open(filename, 'a') as file_object:
        file_object.write(name + '\n')
        print("Your name has been added to the guest book.")


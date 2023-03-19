#3-1. Names:
Names = ['Ali','Usman','Shazam','Zahid']
for i in range(0,len(Names)):
    print(Names[i])


#3-2. Greetings
for i in range(0,len(Names)):
    print("Hello!",Names[i])

#3-3. Your Own List
transport = ['Honda CG150cc','Yamaha R6', 'Suzuki GSXR 1000','Suzuki Hayabusa']
for i in range(0,len(transport)):
    print("I would like to own a",transport[i])

#3-4. Guest List
guest_list = ["Ahmad","Hassan","Qasim","Rimzan"]
for i in range(0,len(transport)):
    print("Hi,", guest_list[i],"I would like to invite you on Dinner!")

#3-5. Changing Guest List
guest_list.remove("Qasim")
guest_list.append("Ali Haider")
for i in range(0,len(transport)):
    print("Hi,", guest_list[i],"I would like to invite you on Dinner!")

#3-6. More Guests
guest_list.insert(0,"Imran")
guest_list.insert(-1,"Haider")
guest_list.append("Safdar")
for i in range(0,len(transport)):
    print("Hi,", guest_list[i],"I would like to invite you on Dinner!")



#3-7. Shrinking Guest List
for i in range(0,len(list())):
    print("I'm Sorry i can't invite you on dinner",guest_list[i])
    guest_list.pop()
    if len(guest_list) <= 2:
        break

for i in range(0,len(guest_list)):
    print("Hi", guest_list[i],"you are stil invited on dinner")

#3-9. Dinner Guests len of guest
print(len(guest_list))

del guest_list


#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.

# Define a list of places to visit
location = ['Makkah','London','Switzerland','New york','England']

# Print the list in its original order
print("Original Order:", location)

# Print the list in alphabetical order using sorted()
print("Alphabetical Order:", sorted(location))

# Show that the original list is still in its original order
print("Original Order:", location)

# Print the list in reverse alphabetical order using sorted()
print("Reverse Alphabetical Order:", sorted(location, reverse=True))

# Show that the original list is still in its original order
print("Original Order:", location)

# Reverse the order of the list using reverse()
location.reverse()
print("Reversed Order:", location)

# Reverse the order of the list again using reverse()
location.reverse()
print("Original Order:", location)

# Sort the list in alphabetical order using sort()
location.sort()
print("Alphabetical Order:", location)

# Sort the list in reverse alphabetical order using sort()
location.sort(reverse=True)
print("Reverse Alphabetical Order:", location)



#3-10. Every Function: Think of something you could store in a list. For example,
#you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items
#and then uses each function introduced in this chapter at least once.

# Create a list of programming languages
languages = ["Python", "Java", "C++", "JavaScript", "Go"]

# Use the append() function to add a new language to the end of the list
languages.append("Ruby")

# Use the insert() function to add a new language at a specific position in the list
languages.insert(2, "PHP")

# Use the remove() function to remove a language from the list
languages.remove("C++")

# Use the pop() function to remove and return the last language from the list
last_language = languages.pop()

# Use the sort() function to sort the list in alphabetical order
languages.sort()

# Use the reverse() function to reverse the order of the list
languages.reverse()

# Use the len() function to get the length of the list
num_languages = len(languages)

# Use a for loop to print each language in the list
print("List of programming languages:")
for language in languages:
    print(language)

# Print the last language that was removed using pop()
print("Last language removed:", last_language)

# Print the length of the list using len()
print("Number of programming languages:", num_languages)

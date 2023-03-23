#6-1. Person

person = {'first_name':'Ali','last_name':'Haider','age':'21','city':'Kasur'}

for key,value in person.items():
    print(key,value)

#6-2. Favorite Numbers:
favorite_numbers = {
    'Ali': 42,
    'Ahmed': 7,
    'Haris': 23,
    'Haider': 16,
    'Hamza': 8,
}

# Print the name and favorite numbers.
for key, value in favorite_numbers.items():
    print(f"{key}'s favorite number is {value}.")


#6-3. Glossary:
glossary = {
    'variable': 'A container that holds a value, which can be of different types (e.g. integer, string, boolean)',
    'list': 'Lists are used to store multiple items in a single variable.',
    'loop': 'A control structure that executes a block of code repeatedly until a certain condition is met',
    'conditional': 'A control structure that allows for different blocks of code to be executed depending on whether a certain condition is met',
    'Tuples': 'Tuple is one of 4 built-in data types in Python used to store collections of data,'
}

# Print the glossary with each word and meaning on separate lines
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")


#6-5. Rivers
# Create the dictionary
rivers = {
    'Jhelum':'Pakistan',
    'nile': 'Egypt',
    'amazon': 'Brazil',
    'yangtze': 'China'
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Print the name of each river
print("\nRivers:")
for river in rivers.keys():
    print(river.title())

# Print the name of each country
print("\nCountries:")
for country in set(rivers.values()):
    print(country.title())

#6-6. Polling
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}

people_to_poll = ['jen', 'sarah', 'edward', 'phil', 'david', 'julia']

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"{person.title()}, we invite you to take the poll and share your favorite programming language.")


#6-7. People

person1 = {'first_name':'Ali','last_name':'Haider','age':21,'city':'Kasur'}
person2 = {'first_name': 'Ahmed', 'last_name': 'Abbas', 'age': 23,'city':'Lahore'}
person3 = {'first_name': 'Hamza', 'last_name': 'Jaffar', 'age': 22,'city':'Karachi'}

# Store all dictionaries in a list called 'people'
people = [person1, person2, person3]


for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")


#6-8. Pets
# Create the list of pets
pets = [
    {"name": "Fido", "animal": "dog", "owner": "Ali"},
    {"name": "Whiskers", "animal": "cat", "owner": "Jawad"},
    {"name": "Black Panther", "animal": "Lion", "owner": "Shahbaz"}
]

# Loop through the list and print out each pet's information
for pet in pets:
    print(f"{pet['name']} is a {pet['animal']} owned by {pet['owner']}.")

#6-9. Favorite Places
# Create the dictionary of favorite places
favorite_places = {
    "Asif": ["Paris", "Hawaii", "New York"],
    "Nadir": ["Tokyo", "Sydney"],
    "Afzal": ["Maldives","California"]
}

# Loop through the dictionary and print each person's name and their favorite places
for person, places in favorite_places.items():
    print(f"{person}'s favorite places are: ")
    for place in places:
        print(f"- {place}")

#6-11. Cities
# Create the dictionary of cities
cities = {
    "New York": {"country": "United States", "population": 8399000, "fact": "The Statue of Liberty is located in New York Harbor."},
    "Tokyo": {"country": "Japan", "population": 13929286, "fact": "Tokyo is the world's largest city by population."},
    "Paris": {"country": "France", "population": 2148000, "fact": "Paris is known as the City of Light."}
}

# Loop through the dictionary and print each city's name and its information
for city, info in cities.items():
    print(f"{city}:")
    print(f"- Country: {info['country']}")
    print(f"- Population: {info['population']}")
    print(f"- Fact: {info['fact']}")

#8-1. Message

#creating Function
def display_message():
    print("Hey! We are learning about functions")

#calling Function
display_message()


#8-2. Favorite Book

#creating function
def favorite_book(title):
    print("One of my favorite books is",title)

#calling function and passing the book title as a function parameter
favorite_book('Alice in Wonderland.')


#8-3. T-Shirt
def make_shirt(size, message):
    """Prints a summary of the shirt size and message."""
    print(f"The shirt size is {size} and it says '{message}' on it.")

# Call the function using positional arguments
make_shirt("M", "Hello, World!")

# Call the function using keyword arguments
make_shirt(size="L", message="Python is cool!")



#8-4. Large Shirts
def make_shirt(message="I love Python", size="L"):
    """Prints a summary of the shirt size and message."""
    print(f"The shirt size is {size} and it says '{message}' on it.")

# Call the function to create a large shirt with default message
make_shirt()

# Call the function to create a medium shirt with default message
make_shirt(size="M")

# Call the function to create a shirt of any size with a different message
make_shirt(size="S", message="Python is awesome!")


#8-5. Cities
def describe_city(city, country='USA'):
    print(f"{city} is in {country}.")

# Example calls to the function
describe_city("New York City")
describe_city("Paris", "France")
describe_city("Sydney", "Australia")

#8-6. City Names

def city_country(city, country):
    return f"{city.title()}, {country.title()}"

# Example calls to the function
print(city_country("santiago", "chile"))
print(city_country("paris", "france"))
print(city_country("tokyo", "japan"))

#8-7. Album:
def make_album(artist_name, album_title, num_tracks=None):
    album_dict = {'artist': artist_name, 'title': album_title}
    if num_tracks:
        album_dict['tracks'] = num_tracks
    return album_dict

# Example calls to the function
album1 = make_album("The Beatles", "Abbey Road")
album2 = make_album("Pink Floyd", "The Wall", 26)
album3 = make_album("Led Zeppelin", "IV")

print(album1)
print(album2)
print(album3)


#8-9. Magicians

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

# Example usage of the function
magicians = ["David Copperfield", "Penn & Teller", "Criss Angel"]
show_magicians(magicians)

#8-10. Great Magicians
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i]

magicians = ['Harry Houdini', 'David Copperfield', 'Penn Jillette', 'Teller', 'David Blaine']
make_great(magicians)
show_magicians(magicians)

#8-12. Sandwiches:
def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print("- " + item)

make_sandwich("turkey", "lettuce", "tomato", "mayonnaise")
make_sandwich("ham", "cheese", "mustard")
make_sandwich("peanut butter", "jelly")


#8-14. Cars

def make_car(manufacturer, model_name, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model_name
    for key, value in car_info.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

#9-1. Restaurant

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("Monal", "Pakistani")
print("Restaurant Name:", restaurant.restaurant_name)
print("Cuisine Type:", restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


#9-2. Three Restaurants:
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant1 = Restaurant("Monal", "Pakistani")
restaurant2 = Restaurant("Pizza Palace", "Italian")
restaurant3 = Restaurant("Burger Barn", "American")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


#9-3. Users: 
class User:
    def __init__(self, first_name, last_name, age, location, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Occupation: {self.occupation}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

user1 = User("Ali", "Haider", 22, "Lahore", "Software Engineer")
user2 = User("Ahmed", "Khan", 23, "Karachi", "Graphic Designer")
user3 = User("Hamza", "Ali", 25, "Muree", "Marketing Manager")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

#9-4. Number Served:
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
        print(f"Number of customers served: {self.number_served}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number
        print(f"Number of customers served has been set to {self.number_served}.")

    def increment_number_served(self, increment):
        self.number_served += increment
        print(f"Number of customers served has been incremented by {increment} to {self.number_served}.")

restaurant = Restaurant("Tasty Bites", "Indian")
restaurant.describe_restaurant()

restaurant.number_served = 20
restaurant.describe_restaurant()

restaurant.set_number_served(50)
restaurant.describe_restaurant()

restaurant.increment_number_served(30)
restaurant.describe_restaurant()


#9-5. Login Attempts:
class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Login attempts: {self.login_attempts}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Login attempts incremented to {self.login_attempts}.")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Login attempts have been reset to 0.")

user1 = User("John", "Doe", 30, "johndoe@example.com")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

user1.describe_user()

user1.reset_login_attempts()

user1.describe_user()


#9-6. Ice Cream Stand: 
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry', 'mint chocolate chip']

    def display_flavors(self):
        print("We have the following flavors of ice cream:")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice_cream_stand = IceCreamStand("Baskin Robbins")
ice_cream_stand.display_flavors()


#9-7. Admin
class User:
    def __init__(self, first_name, last_name, age, gender, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is a {self.age}-year-old {self.gender} who works as a {self.occupation}.")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Login attempts: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login attempts reset to {self.login_attempts}.")

class Admin(User):
    def __init__(self, first_name, last_name, age, gender, occupation):
        super().__init__(first_name, last_name, age, gender, occupation)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Administrator {self.first_name} has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin = Admin("Ali", "Haider", 23, "male", "administrator")
admin.show_privileges()



#9-8. Privileges:
class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        print("Administrator privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


#9-9. Battery Upgrade

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 85:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_electric_car = ElectricCar('tesla', 'model s', 2022)
my_electric_car.battery.get_range()

my_electric_car.battery.upgrade_battery()
my_electric_car.battery.get_range()

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name.title()}")
        print(f"Cuisine type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print("The restaurant is open.")

    def read_number_served(self):
        print(f"Customers served: {self.number_served}")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, number):
        self.number_served += number



restaurant = Restaurant('pizza hut', 'pizza')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.read_number_served()

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(14)
restaurant.read_number_served()
restaurant.increment_number_served(80)
restaurant.read_number_served()
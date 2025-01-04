class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name.title()}")
        print(f"Cuisine type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print("The restaurant is open.")

restaurant_one = Restaurant('pizza hut', 'pizza')
print(restaurant_one.restaurant_name)
print(restaurant_one.cuisine_type)

restaurant_one.describe_restaurant()
restaurant_one.open_restaurant()

restaurant_three = Restaurant('paul\'s place', 'american')
print(restaurant_three.restaurant_name)
print(restaurant_three.cuisine_type)

restaurant_three.describe_restaurant()
restaurant_three.open_restaurant()

restaurant_two = Restaurant('taco bell', 'mexican')
print(restaurant_two.restaurant_name)
print(restaurant_two.cuisine_type)

restaurant_two.describe_restaurant()
restaurant_two.open_restaurant()
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"First name: {self.first_name}, Last name: {self.last_name}")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

name_one = User('raymond', 'lozano')
name_one.greet_user()
name_one.describe_user()
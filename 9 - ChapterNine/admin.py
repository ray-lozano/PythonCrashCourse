class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"First name: {self.first_name}, Last name: {self.last_name}")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("\nList of privileges: ")
        for privilege in self.privileges:
            print(privilege)

class Privileges:
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        print("\nList of privileges: ")
        for privilege in self.privileges:
            print(privilege)

#admin = Admin('raymond', 'lozano')
#admin.show_privileges()

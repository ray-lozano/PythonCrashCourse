class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.privilege = Privileges()

    def describe_user(self):
        print(f"First name: {self.first_name}, Last name: {self.last_name}")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")   

class Privileges:
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        print("\nList of privileges: ")
        for privilege in self.privileges:
            print(privilege)

admin = User('raymond', 'lozano')
admin.privilege.show_privileges()
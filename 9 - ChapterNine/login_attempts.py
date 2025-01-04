class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"First name: {self.first_name}, Last name: {self.last_name}")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

    def read_login_attempts(self):
        print(f"Login attempt(s): {self.login_attempts}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

name = User('raymond', 'lozano')
name.increment_login_attempts()

for x in range(1, 10):
    name.increment_login_attempts()
    name.read_login_attempts()

name.reset_login_attempts()
name.read_login_attempts()
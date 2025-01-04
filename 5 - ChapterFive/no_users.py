#user_names = ['admin', 'raimoondo', 'dyoar', 'sydney', 'mallwin']
user_names = []

if user_names:
    for name in user_names:
        if name == 'admin':
            print(f"Hello {name}, would you like to see a status report?")
        else:
            print(f"Hello {name.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")
user_names = ['admin', 'raimoondo', 'dyoar', 'sydney', 'mallwin']

for name in user_names:
    if name == 'admin':
        print(f"Hello {name}, would you like to see a status report?")
    else:
        print(f"Hello {name.title()}, thank you for logging in again.")
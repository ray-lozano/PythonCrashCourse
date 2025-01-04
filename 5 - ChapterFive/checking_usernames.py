current_users = ['raymond', 'sydney', 'dyoar', 'mallwin', 'thyethye']
new_users = ['justin', 'xxpussyslayer42060xx', 'ladyscrunkles', 'dyoar', 'raymond']

for user in new_users:
    if user in current_users:
        print("Enter a new username, that one is taken.")
    else:
        print("Username available")
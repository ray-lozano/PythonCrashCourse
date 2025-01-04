favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

coders = ['erin', 'erik', 'raymond', 'sydney', 'jen', 'edward', 'sarah']

for coder in coders:
    if coder in favorite_languages.keys():
        print(f"Thank you for taking the poll {coder}")
    else:
        print(f"Please take the poll {coder}.")
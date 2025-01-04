rivers = {'nile': 'egypt', 'amazon': 'south america', 'yangtze': 'china'}

for key, value in rivers.items():
    print(f"The {key.title()} river runs through {value.title()}")
for key in rivers.keys():
    print(key.title())
for value in rivers.values():
    print(value.title())
active = True

while active:
    prompt = "Enter your age for movie ticket pricing. Type 'quit' to quit: "
    age = input(prompt)

    if age == 'quit':
        active = False
    elif int(age) < 3:
        print("Tickets are free.")
    elif int(age) >= 3 and int(age) <= 12:
        print("Tickets are $10")
    else:
        print("Tickets are $15.")
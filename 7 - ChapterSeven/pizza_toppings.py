active = True

while active:
    prompt = "What pizza topping would you like to add? "
    prompt += "\nType 'quit' to quit\n"
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"{topping.title()} added to pizza.")


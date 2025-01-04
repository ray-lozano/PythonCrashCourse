my_pizza = ['pepperoni', 'cheese', 'supreme']
friend_pizzas = my_pizza[:]

my_pizza.append('meat lovers')
friend_pizzas.append('hawaiian')

print("My favorite pizzas are:")
for pizza in my_pizza:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

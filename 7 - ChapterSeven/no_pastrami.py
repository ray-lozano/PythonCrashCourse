sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'pb&j', 'pastrami', 'meatball']
finished_sandwiches = []

print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)
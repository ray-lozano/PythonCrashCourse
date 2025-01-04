import random

lotto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_numbers = []
count = 1


my_ticket = ['a', 'a', 3, 7]

while True:
    for x in range(4):
        winning_numbers.append(random.choice(lotto))
    print("Here are the winning numbers: ")
    print(winning_numbers)

    if my_ticket == winning_numbers:
        print(f"It took {count} loops, until you go the winning numbers.")
    else:
        count += 1


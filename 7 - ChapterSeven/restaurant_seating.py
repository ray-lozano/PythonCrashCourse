seating = input("How many people are in your dinner group? ")
seating = int(seating)

if seating > 8:
    print("\nYou will need to wait for a table")
else:
    print("Your table is ready")
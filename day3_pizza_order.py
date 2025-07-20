print("Welcome to Python Pizza Deliveries")
bill = 0

size = input("What size pizza do you want? S, M, or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# Base price by pizza size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

# Add-ons
if pepperoni == "Y":
    bill += 2

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")

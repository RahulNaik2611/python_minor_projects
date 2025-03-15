#pizza delivary s = $150 ,M = $200,L=$250 , pepperoni = $30 , Extra_Chessa = $50

print("Welcome to Pizza Deliveries!")

# Initialize the bill variable
bill = 0

# User inputs
Size = input("What size pizza do you want? S, M, or L ===> ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N ===> ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ===> ").lower()

# Calculate cost based on size
if Size == 'S':
    bill += 150
elif Size == 'M':
    bill += 200
elif Size == 'L':
    bill += 250
else:
    print("You typed the wrong input.")

# Add cost of pepperoni
if pepperoni == 'y':
    if Size == 'S':
        bill += 30
    else:
        bill += 35

# Add cost of extra cheese
if extra_cheese == 'y':
    bill += 45

# Final bill
if bill > 0:
    print(f"Your final bill is: ₹{bill}.")
else:
    print("Please restart and enter valid inputs.")


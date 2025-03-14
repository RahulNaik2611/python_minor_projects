print("Welcome to the tip  calculator ")

bill = float(input("What was the total bill ? 💸 INR" + "  "))

tip = int(input("What percentage tip would you give 10,12 & 15" + " "))

people = int(input("How many people want to split bill " + " "))

bill_with_tip = (tip /100) * bill + bill

bill_per_person = bill_with_tip / people

Final_amount = round(bill_per_person,2)

print(f"Each person should pay {Final_amount} ")

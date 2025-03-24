import random


while True:
    choice = input("Roll the dice ? (y/n) :   ").lower()
    if choice == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)

        print(die1,die2)

    elif choice == 'n':
        print("Thanks For Playing")
        break
    else:
        print("invalid choices")

import  random



number_To_guess = random.randint(1,100)

while True:
    try:
        Guess = int(input("Enter the number here : "))

        if Guess < number_To_guess:
            print("Too low!")
        elif Guess > number_To_guess:
            print("Too high")
        else:
            print("Congratulations! you guessing the number.")
            break                         



    except ValueError:
        print("Please Entre a valid number ")




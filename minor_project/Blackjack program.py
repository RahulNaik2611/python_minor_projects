import random


def print_card(card):
    """Prints a single card in ASCII art"""
    if card == 10:  # Face cards (Jack, Queen, King) and 10
        card_str = "10"
    elif card == 11:
        card_str = "A "
    else:
        card_str = f"{card} "

    print(f"┌───────┐")
    print(f"| {card_str}    |")
    print(f"|       |")
    print(f"|    {card_str} |")
    print(f"└───────┘")


def print_hand(hand, hide_first=False):
    """Prints all cards in a hand"""
    print("Current hand:")
    for i, card in enumerate(hand):
        if hide_first and i == 0:
            print("┌───────┐")
            print("| ░░░░░ |")
            print("| ░░░░░ |")
            print("| ░░░░░ |")
            print("└───────┘")
        else:
            print_card(card)


def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Calculate the score of a hand"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Compare scores and determine the winner"""
    if u_score == c_score:
        return "It's a Draw! 😒"
    elif c_score == 0:
        return "You lose, opponent has Blackjack!"
    elif u_score == 0:
        return "Blackjack! You win! 🎉"
    elif u_score > 21:
        return "You went over 21. You lose!"
    elif c_score > 21:
        return "Opponent went over 21. You win! 🎉"
    elif u_score > c_score:
        return "You win! 🎉"
    else:
        return "You lose! 🤣"


def play_game():
    """Main game function"""
    print("""
    Welcome to Blackjack!
    Try to get as close to 21 as possible without going over.
    Aces count as 11 or 1, face cards count as 10.
    """)

    user_hand = []
    computer_hand = []
    is_game_over = False

    # Deal initial cards
    for _ in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)

        print("\n" + "=" * 30)
        print("Your hand:")
        print_hand(user_hand)
        print(f"Your current score: {user_score}\n")

        print("Computer's hand:")
        print_hand(computer_hand, hide_first=True)
        print()

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("Type 'h' to Hit (get another card), 's' to Stand: ").lower()
            if user_choice == 'h':
                user_hand.append(deal_card())
            elif user_choice == 's':
                is_game_over = True
            else:
                print("Invalid input. Please type 'h' or 's'.")

    # Computer's turn to play
    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print("\n" + "=" * 30)
    print("Final Results:")
    print("Your final hand:")
    print_hand(user_hand)
    print(f"Your final score: {user_score}\n")

    print("Computer's final hand:")
    print_hand(computer_hand)
    print(f"Computer's final score: {computer_score}\n")

    print(compare(user_score, computer_score))
    print("=" * 30 + "\n")

    # Ask to play again
    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again == 'y':
        play_game()
    else:
        print("Thanks for playing!")


# Start the game
play_game()
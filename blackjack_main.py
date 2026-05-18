
def blackjack():
    import random
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    game_start = True

    def hand_calculation(hand):
        score = sum(hand)
        if score > 21 and 11 in hand:
                hand.remove(11)
                hand.append(1)
                score = sum(hand)
        return score

#the first part of the game
    question = str(input("Do you want to play a game of Black Jack 'y' or 'n'?\n")).lower()
    while game_start:
        if question == "y":
            your_cards = []
            computer_cards = []
            card_drawl = True
            print("\n" * 20)
            from art import logo
            print(logo)

            for card in range(0,2):
                your_cards.append(random.choice(cards))
                your_total = hand_calculation(your_cards)
            print(f"your cards: {your_cards}, current score is {your_total}")

            for card in range(0,2):
                computer_cards.append(random.choice(cards))
                computer_first_card = computer_cards[0]
                computer_total = hand_calculation(computer_cards)

            print(f"Computer's first card: {computer_first_card}")
#the users turn
            while card_drawl:
                if your_total < 21:
                    question2 = str(input("Type 'y' to get another card or type 'n' to pass")).lower()
                    if question2 == "y":
                        card_drawl = True
                        your_cards.append(random.choice(cards))
                        your_total = hand_calculation(your_cards)
                        print(f"your hand: {your_cards}, current score is {your_total}")
                    if question2 == "n":
                        card_drawl = False
                else:
                    card_drawl = False
#computer's turn
            while computer_total < 17:
                    computer_cards.append(random.choice(cards))
                    computer_total = hand_calculation(your_cards)
                    print(f"Computer's final hand: {computer_cards}, current score is {computer_total}")


            if your_total > 21:
                print("You went over, Computer wins")
            elif computer_total > 21:
                print("Computer Bust! YOU WON!")
            elif computer_total == your_total:
                print("Draw!")
            elif your_total > computer_total:
                print("You won!")
            else:
                print("Computer wins!")

            question = input("Would you like to play again?").lower()


        else:
            game_start = False
            print("GOODBYE!")
            break

blackjack()


# --- THE 2 BIG FIXES ---

# FIX 1: THE RESET (Inside the 'if question == "y"' block)
# You must set these to [] at the start of every round.
# If they are outside the loop, the computer "remembers" old cards.
# your_cards = []
# computer_cards = []
# card_drawl = True  <-- This must be True to "re-open" the player's turn.

# FIX 2: THE BREAK (At the very bottom of the game)
# You must OVERWRITE the 'question' variable.
# If you just use 'input()', the 'question' stays as "y" forever.
# By using 'question = input().lower()', you change the "battery."
# If the user types "n", the 'if' fails, the 'else' triggers, and the 'break' works.












import random
from shape import shape

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(card_list):
    score = sum(card_list)
    if 11 in card_list and score > 21:
        card_list[card_list.index(11)] = 1
        score = sum(card_list)
    return score

game_status = True
while game_status:
    game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


    if game_start == 'y':

        print(shape)

        player_cards = [random.choice(cards), random.choice(cards)]
        computer_cards = [random.choice(cards), random.choice(cards)]

        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\n\tYour cards: {player_cards}, current score: {player_score}")
        print(f"\tOpponent's first card: {computer_cards[0]}\n")


        while player_score < 21:
            game_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if game_continue == 'y':
                new_card = random.choice(cards)
                player_cards.append(new_card)
                player_score = calculate_score(player_cards)
                print(f"Your cards: {player_cards}, current score: {player_score}")
            elif game_continue == 'n':
                break


        while computer_score < 17:
            new_card = random.choice(cards)
            computer_cards.append(new_card)
            computer_score = calculate_score(computer_cards)


        print(f"\n\tYour final hand: {player_cards}, final score: {player_score}")
        print(f"\tOpponent's final hand: {computer_cards}, final score: {computer_score}\n")

        if player_score > 21:
            print(" You went over 21... You lose! ❌\n")
        elif computer_score > 21:
            print(" Opponent went over 21... You win! 🏆\n")
        elif player_score > computer_score:
            print(" You win! Great job! 🎊\n")
        elif player_score < computer_score:
            print(" Opponent wins. Better luck next time! 🤷‍♂️ \n")
        else:
            print(" It's a draw! ⚖️\n")

    else:
        game_status = False
        print("Game ended.")

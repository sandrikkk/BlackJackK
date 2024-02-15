import random


def random_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


def players_cards_sum(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 'BlackJack'
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(computer_points, player_points):
    if computer_points == player_points:
        return 'Draw !'
    elif computer_points == 'BlackJack':
        return 'You lose :('
    elif player_points == 'BlackJack':
        return "You won !"
    elif player_points > 21:
        return "You lose you have more than 21 points !"
    elif computer_points > 21:
        return "You win yoo, your bitch opponent has more than 21 points !"
    elif player_points > computer_points:
        return 'You win !'
    else:
        return 'You lose !'


def main_menu():
    player_card = []
    computer_card = []
    player_points = 0
    computer_points = 0
    game_status = True
    for _ in range(2):
        player_card.append(random_cards())
        computer_card.append(random_cards())

    while game_status:
        player_points = players_cards_sum(player_card)
        computer_points = players_cards_sum(computer_card)
        print(f"Player Cards are : {player_card} and sum is {player_points}")
        print(f"computer Card is : {computer_card[0]}")
        if player_points == 'BlackJack' or computer_points == 'BlackJack':
            print("You Win !")
            game_status = False
        else:
            offer = input('if you want to pick card click y button if not click n button :')
            if offer == 'y':
                player_card.append(random_cards())
            else:
                game_status = False

    while computer_points != 0 and computer_points < 17:
        computer_card.append(random_cards())
        computer_points = players_cards_sum(computer_card)
    print(f"Computer final cards are : {computer_card} and points are {computer_points}")
    print(compare(computer_points, player_points))


while input('do you want to start game ? (n) or (y) :') == 'y':
    main_menu()

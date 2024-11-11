from blackjack_helper import *

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

# initialize game interface and asl for number of players
no_players = int(input('Welcome to Blackjack! How many players? '))

# dictionary to contain player names and scores
player_names = {}

for player in range(no_players):
    # ask for player name and add capitalized form of the name for uniformity
    # add one so that the numbers correspond to what users like to see
    player_name = input(f'Player {player + 1} name: ')
    # add the player as a the dictionary
    player_names[player_name.upper()] = {}

    # USER'S GAME PLAY
    '''
    This function will be used to intitialize each users game
    without having to loop multiple times
    '''


def user_interface(player):
    user_hand = draw_starting_hand(f"{player}'S")
    should_hit = 'y'
    while user_hand < 21:
        should_hit = input(f"{player}, you have {user_hand}. Hit (y/n)? ")
        if should_hit == 'n':
            break
        elif should_hit != 'y':
            print("Sorry I didn't get that.")
        else:
            user_hand = user_hand + draw_card()
    print_end_turn_status(user_hand)

    # contain the user's hand value
    return user_hand


should_continue = 'y'

while should_continue == 'y':

    # update the dictionary to contain their scores and current hand value
    for player in player_names:
        player_names[player]['hand'] = 0
        player_names[player]['score'] = 3
    # this dictionary contains the score and hand

    for player in player_names:
        player_hand = user_interface(player)
        player_names[player]['hand'] = player_hand

    # DEALER'S TURN
    dealer_hand = draw_starting_hand("DEALER'S")
    while dealer_hand < 17:
        print("Dealer has {}.".format(dealer_hand))
        dealer_hand = dealer_hand + draw_card()
    print_end_turn_status(dealer_hand)

    print_header('GAME RESULT')

    # Game result for every player
    for player in player_names:
        # print a customized result
        # player hand is held in the corresponding dictionary key

        # collect the winner of the game
        output = print_end_game_status(player_names[player]['hand'], dealer_hand, player)

        if output == 'push':
            # don't  add or subtract anything if it's push
            print(f" Score: {player_names[player]['score']}")
        elif output == None:
            player_names[player]['score'] -= 1  # subtract 1 if dealer wins
            print(f" Score: {player_names[player]['score']}")
        elif output == player:
            player_names[player]['score'] += 1  # add one if user wins
            print(f" Score: {player_names[player]['score']}")
        if player_names[player]['score'] == 0:
            print(f'{player} eliminated!')
            del player_names[player]

    should_continue = input('Do you want to play another hand (y/n)? ')
    if should_continue == 'n':
        break
    elif player_names == {}:
        print('All players eliminated!')
        break


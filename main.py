from funcs import *


def logic():
    global board, player1, player2

    print(board)
    used_val = []
    print('Player1 is x | Player 2 is o')

    while True:

        player1_choice = input('Player1: ')
        while player1_choice not in positions:
            if player1 not in positions:
                print('Player1 please input a number from 1-9')
            player1_choice = input('Player1: ')
        w1 = input_player_choice_in_board(player1_choice, 'x', 'player1')
        print(w1)
        if player1_choice in used_val:
            continue

        if no_spot_left():
            print('No one won')
            break

        winner = get_winner()
        if winner:
            print(winner)
            break

        player2_choice = input('Player2: ')
        while player2_choice not in positions:
            player2_choice = input('Player2: ')
        w2 = input_player_choice_in_board(player2_choice, 'o', 'player2')
        print(w2)
        used_val.append(w1)

        while player2_choice in used_val:
            player2_choice = input('Player2: ')
            w2 = input_player_choice_in_board(player2_choice, 'o', 'player2')
            print(w2)
        used_val.append(w2)

        winner = get_winner()
        if winner:
            print(winner)
            break


if __name__ == '__main__':
    logic()

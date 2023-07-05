# Tic tac toe board
board = """
|1|2|3|
|4|5|6|
|7|8|9|
"""

positions = [str(ch) for ch in range(1, 10)]

player1 = 'x'
player2 = 'o'


def check_player_inputs(player1: str, player2: str):
    if not player_1.isdigit():
        return False
    return True


def get_players(player1: str, player2: str):
    print(f'Player1 (x): {player1}\n player2: (o) {player2}')


def input_player_choice_in_board(player_choice: str, rep: str, player: str = 0):
    global board
    try:
        if board[board.index(player_choice)].isdigit():
            board = board.replace(player_choice, rep)
            print(board)
            return player_choice
    except ValueError:
        return (f'Position is already taken {player}')


def check_winner(po1, po2, po3):
    if po1 == 'x' and po2 == 'x' and po3 == 'x':
        return 'player1 wins'
    if po1 == 'o' and po2 == 'o' and po3 == 'o':
        return 'player2 wins'


def get_winner():

    one = check_winner(board[2], board[4], board[6])
    two = check_winner(board[10], board[12], board[14])
    three = check_winner(board[18], board[20], board[22])

    four = check_winner(board[2], board[10], board[18])
    five = check_winner(board[4], board[12], board[20])
    six = check_winner(board[6], board[14], board[22])

    seven = check_winner(board[2], board[12], board[22])
    eight = check_winner(board[6], board[12], board[18])

    outcomes = [one, two, three, four, five, six, seven, eight]
    winner = list(filter(lambda x: x != None, outcomes))
    if len(winner) > 0:
        return winner[0]


def no_spot_left():
    spot = list(filter(lambda x: x.isdigit(), board))
    if len(spot) == 0:
        return True

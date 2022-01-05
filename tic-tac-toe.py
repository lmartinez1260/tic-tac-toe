import random

board = ['-'] * 9
player_1_name = ""
player_2_name = ""

X_symbol = True
O_symbol = False

# True is X, False is O
def random_player():
    return bool(random.randint(0, 1))

def print_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print("-" * 10)
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print("-" * 10)
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

# Returns the symbol of the winner if it exists, if there is no winner then returns false
# Example: returns X if X is the winner
"""
0 1 2
3 4 5
6 7 8
"""
def winner_exists():
    # Do all the horizontals
    if board[0] == board[1] and board[1] == board[2] and board[0] != '-':
        return board[0]
    if board[3] == board[4] and board[4] == board[5] and board[3] != '-':
        return board[3]
    if board[6] == board[7] and board[7] == board[8] and board[6] != '-':
        return board[6]

    # Do all the verticals 
    if board[0] == board[3] and board[3] == board[6] and board[0] != '-':
        return board[0]
    if board[1] == board[4] and board[4] == board[7] and board[1] != '-':
        return board[1]
    if board[2] == board[5] and board[5] == board[8] and board[2] != '-':
        return board[2]

    # Do the diagonals
    if board[0] == board[4] and board[4] == board[8] and board[0] != '-':
        return board[0]
    if board[2] == board[4] and board[4] == board[6] and board[2] != '-':
        return board[2]
    return False

# True if board is full, False is board is not full
def is_board_full():
    return not '-' in board

# Assuming the game is over, return the winner or if there is a tie
def game_winner():
    winner = winner_exists()
    if winner == 'X':
        return player_1_name
    elif winner == 'O':
        return player_2_name
    else: return "Tie"

def game_loop():
    current_player = random_player()
    while not winner_exists() and not is_board_full():
        print_board()

        # Printing what the user should enter next
        if current_player:
            print("Current turn is (X) " + player_1_name)
        else:
            print("Current turn is (O)  " + player_2_name)
        mark = int(input("Select a spot in the board between 1-9, not previously selected: ")) - 1

        # Error checking
        if mark < 0 or mark > 8:
            print("Mark is an invalid move, should be between [1, 9]")
            continue
        if board[mark] != '-':
            print("Mark is already occupied")
            continue

        # Place the symbol on the board
        if current_player == X_symbol:
            board[mark] = 'X'
        elif current_player == O_symbol:
            board[mark] = 'O'
        # current_player is opposite of what it is, so the alternating behavior
        current_player = not current_player
    # At this point, there is either a tie or a winner

    print("ENDING STATE BOARD")
    print_board()
    winner = game_winner()
    if winner == "Tie":
        print("There was a tie!")
    else: print("The winner is " + winner)
    print("")

# -- Actual code below --
player_1_name = input("Enter name for player 1, will be X: ")
player_2_name = input("Enter name for player 2, will be O: ")


# # If true, there is a game in progress
match = True
while match:
    board = ['-'] * 9
    game_loop()
    match = bool(input("Enter anything if you to play another match"))

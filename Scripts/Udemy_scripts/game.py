#!/usr/bin/env python3

'''
This script makes a noughts and crosses game (tic, tac, toe).
Player 1 and user 2 pick board numbers between 1 and 9 (specified in print_board function).
When one player has three in a row horizontally, vertically or diagonally they are declared winner.
If not one wins a draw is declared.
'''

# generates spaces for the board using list comprehensions
board = [" " for i in range(9)]
# function to make board 3 x 3
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# Function that provides connection between icon X or O with player 1 or 2
def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    print("Your turn player {}".format(number))
    
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice -1] == " ":
        board[choice -1] = icon
    else:
        print()
        print("That space is taken!")

# Function that sets out combinations where an icon can win - parallel, horizontal, and diagonal.
def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] ==icon) or \
        (board[3] == icon and board[4] == icon and board[5] ==icon) or \
        (board[6] == icon and board[7] == icon and board[8] ==icon) or \
        (board[0] == icon and board[3] == icon and board[6] ==icon) or \
        (board[1] == icon and board[4] == icon and board[7] ==icon) or \
        (board[2] == icon and board[5] == icon and board[8] ==icon) or \
        (board[0] == icon and board[4] == icon and board[8] ==icon) or \
        (board[2] == icon and board[4] == icon and board[6] ==icon):
        return True
    else:
        return False

# Function if the game completes without a winner
def is_draw():
    if " " not in board:
        return True
    else:
        return False

# Loop that controls the game play and checks for winers calling is_victory function
while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print ("X wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    player_move("O")
    if is_victory("O"):
        print_board()
        print ("O wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break

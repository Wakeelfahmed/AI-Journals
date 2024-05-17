import matplotlib.pyplot as plt
import numpy as np


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file = pd.read_csv(filepath_or_buffer='fsd.csv')













import math

# Function to print the game board
def print_board(board):
    for row in board:
        print(" | ".join(row))
-        print("-" * 10)


# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


# Function to check if the game is over
def game_over(board):
    return any(check_winner(board, player) for player in ['X', 'O']) or all(
        all(cell != '.' for cell in row) for row in board)


# Function to evaluate the board state
def evaluate(board):
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    else:
        return 0


# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, alpha, beta, maximizingPlayer):
    if game_over(board) or depth == 0:
        return evaluate(board)

    if maximizingPlayer:
        maxEval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = 'X'
                    eval = minimax(board, depth - 1, alpha, beta, False)
                    board[i][j] = '.'
                    maxEval = max(maxEval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return maxEval
    else:
        minEval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                    eval = minimax(board, depth - 1, alpha, beta, True)
                    board[i][j] = '.'
                    minEval = min(minEval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return minEval


# Function to find the best move using minimax with alpha-beta pruning
def find_best_move(board):
    bestMove = (-1, -1)     # row & col
    bestEval = -math.inf
    alpha = -math.inf
    beta = math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                board[i][j] = 'X'
                eval = minimax(board, 5, alpha, beta, False)
                board[i][j] = '.'
                if eval > bestEval:
                    bestEval = eval
                    bestMove = (i, j)
    return bestMove


# Main function to play the game
# Start the game
board = [['.' for _ in range(3)] for _ in range(3)]  # create board
print("Let's play Tic Tac Toe!")

print_board(board)

while not game_over(board):
    x, y = map(int, input("Enter your move (row and column, separated by space): ").split())
    if board[x][y] != '.':
        print("Invalid move! Try again.")
        continue
    board[x][y] = 'O'
    print_board(board)
    if game_over(board):
        break
    print("Computer's turn:")
    bestMove = find_best_move(board)
    board[bestMove[0]][bestMove[1]] = 'X'
    print_board(board)

if check_winner(board, 'X'):
    print("Computer wins!")
elif check_winner(board, 'O'):
    print("You win!")
else:
    print("It's a draw!")
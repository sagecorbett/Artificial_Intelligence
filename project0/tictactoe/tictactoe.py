"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    total_moves = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'X' or board[i][j] == 'O':
                total_moves += 1

    if total_moves % 2 == 0:
        return 'X'
    else:
        return 'O'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    all_possible_moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                all_possible_moves.append((i,j))

    if len(all_possible_moves) > 0:
        return set(all_possible_moves)
    else:
        return None

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copy_of_board = board[:]
    possible_moves = actions(board)
    # If action is not a valid action for the board, your program should raise an exception.
    if action not in possible_moves:
        raise Exception('Not a possible move')
    else:
        copy_of_board[action[0]][action[1]] = player(copy_of_board)
        return copy_of_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # If the X player has won the game, your function should return X. 
    # If the O player has won the game, your function should return O.
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is not EMPTY:
                current_player = board[i][j]

                # Check horizontally 
                if board[i][0] == board[i][1] == board[i][2]:
                    return current_player

                # Check vertically
                if board[0][j] == board[1][j] == board[2][j]:
                    return current_player

                # Check diagonally
                if board[0][0] == current_player and board[0][0] == board[1][1] == board[2][2]:
                    return current_player
                elif board[2][0] == current_player and board[2][0] == board[1][1] == board[0][2]:
                    return current_player

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or actions(board) == None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    board_winner = winner(board)
    if board_winner == 'X':
        return 1
    elif board_winner == 'O':
        return -1
    else: 
        return 0
   


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    

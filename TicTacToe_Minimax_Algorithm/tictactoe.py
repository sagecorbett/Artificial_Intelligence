"""
Tic Tac Toe Player
"""

import math
import copy

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
    # return [[EMPTY, O, X],
    #         [X, O, EMPTY],
    #         [O, EMPTY, X]]


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
    copy_of_board = copy.deepcopy(board)
    possible_moves = actions(board)
    # If action is not a valid action for the board, your program should raise an exception.
    if possible_moves == None:
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
    if terminal(board):
        return None

    if player(board) == 'X':
        m = max_value(board)
        return m[1]
    else:
        m = min_value(board)
        return m[1]
    

def max_value(board):
    # This will end the recursion
    if terminal(board):
        return [utility(board), None]

    # Since this is the max value we need to start at -Infinity so that 
    # as we loop through all possible actions we can pick an action that brings us
    # the best value. Therefor value will only ever increase
    value = -math.inf
    best_action = None
    for action in actions(board):
        value_for_current_action = max(value, min_value(result(board, action))[0])
        if value_for_current_action > value:
            value = value_for_current_action
            best_action = action
        # Best possible outcome for the maximizer is 1 so if our value is == 1
        # then we can just take that action and break
        if value == 1:
            break

    return [value, best_action]

def min_value(board):
    # End the recursion

    # this at the end of the recursion this returns a number but if it is not the
    # end of the recursion it returns an array []
    if terminal(board):
        return [utility(board), None]
    
    # Min values goal is to minimize and choose the most negative action found
    value = math.inf
    best_action = None
    for action in actions(board):
        value_for_current_action = min(value, max_value(result(board, action))[0])
        if value_for_current_action < value:
            value = value_for_current_action
            best_action = action

        # Best possible outcome for the minimizer is -1 so if our value is == -1
        # then we can just take that action and break
        if value == -1:
            break
    return [value, best_action]

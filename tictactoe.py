"""
Tic Tac Toe Player
"""

import copy
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
    
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count += 1
    
    if board == initial_state():
        return X
    if count % 2 == 1:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    #idea - recursion detects empty squares and randomly selects a square to fill based on 
    # whose chance it it from player function.
    """
    m = []
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if(board[i][j] == EMPTY):
                m.append((i,j))
    return m

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    a,b = action
    if board[a][b] != EMPTY:
        raise Exception("Invalid action, cell is not empty.")
    n = copy.deepcopy(board)
    n[a][b] = player(board)
    return n


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None
    
def terminal(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(winner(board) is not None):
        return True
    for i in range (0,len(board)):
        for j in range (0,len(board[i])):
            if board[i][j] == EMPTY:
                return False
    return True

def utility(board):
    if(winner(board) == 'X'):
        return 1
    elif(winner(board) == 'O'):
        return -1
    else:
        return 0
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    Max = float("-inf")
    Min = float("inf")

    if player(board) == X:
        return max_value(board, Max, Min)[1]
    else:
        return min_value(board, Max, Min)[1]

def max_value(board, Max, Min):
    if terminal(board):
        return utility(board),None
    v = float('-inf')
    move = None
    for action in actions(board):
        test = min_value(result(board, action), Max, Min)[0]
        Max = max(Max, test)
        if test > v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move]


def min_value(board, Max, Min):
    if terminal(board):
        return utility(board),None
    v = float('inf')
    move = None
    for action in actions(board):
        test = max_value(result(board, action), Max, Min)[0]
        Min = min(Min, test)
        if test < v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move]
    
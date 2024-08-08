
import math
import copy


def terminal(board):
    '''
    We suppose that X is our max player and O is our min player
    '''
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != " ":
            return 1 if board[i][0] == 'X' else -1
        if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != " ":
            return 1 if board[0][i] == 'X' else -1
    if (board[0][0] == board[1][1] == board[2][2] != " ") or (board[2][0] == board[1][1] == board[0][2] != " ") and board[1][1] != " ":
        return 1 if board[1][1] == 'X' else -1
    unfilledSquares = sum(row.count(" ") for row in board)
    if unfilledSquares == 0:
        return 0


def linearToTwoDimensional(index):
    return index//3, index % 3


def actions(board):
    actions = []
    for i in range(9):
        a, b = linearToTwoDimensional(i)
        if board[a][b] == " ":
            actions.append(i)
    return actions


def result(board, action, turn):
    i, j = linearToTwoDimensional(action)
    boardCopy=copy.deepcopy(board)
    boardCopy[i][j] = turn
    return boardCopy


def MiniMax(board, turn):
    terminalValue = terminal(board)
    if (terminalValue != None):
        return None, terminalValue
    if turn == 'X':
        maxi = -math.inf
        maxAction = -1
        for a in actions(board):
            resultingState = result(board, a, turn)
            value = MiniMax(resultingState, "O")[1]

            if value > maxi:
                maxi = value
                maxAction = a
        return maxAction, maxi
    else:
        mini = math.inf
        minAction = -1
        for a in actions(board):
            resultingState = result(board, a, turn)
            value = MiniMax(resultingState, "X")[1]
            if value < mini:
                mini = value
                minAction = a
        return minAction, mini

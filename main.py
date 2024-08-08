import mini_max

board = [[" " for i in range(3)] for i in range(3)]


def count_occupied_squares(board):
    totalOccupied = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != " ":
                totalOccupied += 1
    return totalOccupied


def print_board(board):
    for i in range(3):
        print(' | '.join(board[i]))
        if i != 2:
            print('----------')
    print('\n\n')


def print_board_layout():
    number_board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    print_board(number_board)


def linearToTwoDimensional(index):
    return index//3, index % 3


def winner(board):
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != " ":
            return board[i][0]
        if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != " ":
            return board[0][i]
    if (board[0][0] == board[1][1] == board[2][2] != " ") or (board[2][0] == board[1][1] == board[0][2] != " ") and board[1][1] != " ":
        return board[1][1]
    if count_occupied_squares(board) == 9:
        return 'D'
    return None


def get_computer_move(board, symbol):
    if symbol == 'X':
        # action with maxmimum value
        return mini_max.MiniMax(board, 'X')[0]
    else:
        # action with minimim vale
        return mini_max.MiniMax(board, 'O')[0]


def get_human_move(board):
    square = int(input("Enter a square to mark: "))
    return square-1


def implement_move(board, turn, index):
    i, j = linearToTwoDimensional(index)
    board[i][j] = turn


def show_result(winnerSymbol, humanSymbol):
    if winnerSymbol == 'D':
        print("Its a draw.You are brilliant")
        return
    if winnerSymbol == humanSymbol:
        print("Yep,You a genius.ALthough it might never happen")
        return
    print("Bad luck. Try again later.")


def play(board, humanFirst=True):
    humanSymbol = 'X' if humanFirst else 'O'
    turn = 'X'
    print("Enter the following indices to mark the squares\n")
    print_board_layout()
    print("\nTIC TAC TOE\n\n")

    print_board(board)
    while (winner(board) == None):
        move = -1
        if turn == humanSymbol:
            move = get_human_move(board)
        else:
            move = get_computer_move(board, turn)
        implement_move(board, turn, move)
        print_board(board)
        turn = 'X' if turn == 'O' else 'O'

    show_result(winner(board), humanSymbol)


if __name__ == "__main__":
    play(board)

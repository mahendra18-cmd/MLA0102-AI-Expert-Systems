import math

def print_board(board):
    for r in range(3):
        print(board[r][0], board[r][1], board[r][2])

def check_winner(board):
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] != '_': return board[r][0]
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != '_': return board[0][c]
    if board[0][0] == board[1][1] == board[2][2] != '_': return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '_': return board[0][2]
    return None

def minimax(board, is_max):
    winner = check_winner(board)
    if winner == 'X': return 1
    if winner == 'O': return -1
    if all(cell != '_' for row in board for cell in row): return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, False))
                    board[i][j] = '_'
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, True))
                    board[i][j] = '_'
        return best

board = [['_']*3 for _ in range(3)]
print("Initial Board:")
print_board(board)

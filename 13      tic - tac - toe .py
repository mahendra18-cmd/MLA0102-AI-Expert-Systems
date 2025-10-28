import math

# Initialize empty 3x3 board
board = [' ']*9

def print_board():
    print(f"{board[0]}|{board[1]}|{board[2]}\n-+-+-\n{board[3]}|{board[4]}|{board[5]}\n-+-+-\n{board[6]}|{board[7]}|{board[8]}")

# Check for winner
def check_winner(b):
    for a,b1,c in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]:
        if board[a]==board[b1]==board[c]!=' ': 
            return board[a]
    return None

# Minimax algorithm
def minimax(is_max):
    winner = check_winner(board)
    if winner == 'O': return 1
    if winner == 'X': return -1
    if ' ' not in board: return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i]==' ':
                board[i]='O'
                best=max(best,minimax(False))
                board[i]=' '
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i]==' ':
                board[i]='X'
                best=min(best,minimax(True))
                board[i]=' '
        return best

# AI makes optimal move
def ai_move():
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i]==' ':
            board[i]='O'
            val = minimax(False)
            board[i]=' '
            if val>best_val:
                best_val, move = val, i
    board[move]='O'

# Main Game Loop
while True:
    print_board()
    if check_winner(board) or ' ' not in board:
        print("Winner:", check_winner(board) or "Draw")
        break
    move = int(input("Enter your move (0–8): "))
    if board[move]==' ':
        board[move]='X'
        if not check_winner(board) and ' ' in board:
            ai_move()








OUTPUT :

 | | 
-+-+-
 | |
-+-+-
 | |
Enter your move (0–8): 0
X| | 
-+-+-
 |O|
-+-+-
 | |
Enter your move (0–8): 6
X| | 
-+-+-
O|O|
-+-+-
X| |
Enter your move (0–8): 7
X| | 
-+-+-
O|O|O
-+-+-
X|X|
Winner: O

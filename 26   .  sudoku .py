board=[[5,3,0,0,7,0,0,0,0],
       [6,0,0,1,9,5,0,0,0],
       [0,9,8,0,0,0,0,6,0],
       [8,0,0,0,6,0,0,0,3],
       [4,0,0,8,0,3,0,0,1],
       [7,0,0,0,2,0,0,0,6],
       [0,6,0,0,0,0,2,8,0],
       [0,0,0,4,1,9,0,0,5],
       [0,0,0,0,8,0,0,7,9]]

def valid(b,r,c,n):
    if any(b[r][x]==n for x in range(9)): return False
    if any(b[x][c]==n for x in range(9)): return False
    sr,sc=3*(r//3),3*(c//3)
    for i in range(sr,sr+3):
        for j in range(sc,sc+3):
            if b[i][j]==n: return False
    return True

def solve():
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                for n in range(1,10):
                    if valid(board,i,j,n):
                        board[i][j]=n
                        if solve(): return True
                        board[i][j]=0
                return False
    return True

solve()
for r in board: print(r)



OUTPUT :

[5, 3, 4, 6, 7, 8, 9, 1, 2]
[6, 7, 2, 1, 9, 5, 3, 4, 8]
[1, 9, 8, 3, 4, 2, 5, 6, 7]
[8, 5, 9, 7, 6, 1, 4, 2, 3]
[4, 2, 6, 8, 5, 3, 7, 9, 1]
[7, 1, 3, 9, 2, 4, 8, 5, 6]
[9, 6, 1, 5, 3, 7, 2, 8, 4]
[2, 8, 7, 4, 1, 9, 6, 3, 5]
[3, 4, 5, 2, 8, 6, 1, 7, 9]

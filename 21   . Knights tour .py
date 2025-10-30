N=5
move_x=[2,1,-1,-2,-2,-1,1,2]
move_y=[1,2,2,1,-1,-2,-2,-1]
board=[[-1]*N for _ in range(N)]

def safe(x,y): return 0<=x<N and 0<=y<N and board[x][y]==-1

def solve(x,y,move):
    if move==N*N: return True
    for i in range(8):
        nx,ny=x+move_x[i],y+move_y[i]
        if safe(nx,ny):
            board[nx][ny]=move
            if solve(nx,ny,move+1): return True
            board[nx][ny]=-1
    return False

board[0][0]=0; solve(0,0,1)
for r in board: print(r)



OUTPUT :

[0, 5, 14, 9, 20]
[13, 8, 19, 4, 15]
[18, 1, 6, 21, 10]
[7, 12, 23, 16, 3]
[24, 17, 2, 11, 22]

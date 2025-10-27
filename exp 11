from collections import deque

def valid(m, c):
    return 0 <= m <= 3 and 0 <= c <= 3 and (m == 0 or m >= c) and (3-m == 0 or 3-m >= 3-c)

def bfs():
    start, goal = (3,3,1), (0,0,0)
    q = deque([(start, [start])])
    while q:
        (m,c,b), path = q.popleft()
        if (m,c,b) == goal:
            return path
        sign = -1 if b else 1
        for dm, dc in [(1,0),(2,0),(0,1),(0,2),(1,1)]:
            nm, nc, nb = m + sign*dm, c + sign*dc, 1-b
            if valid(nm, nc):
                state = (nm,nc,nb)
                if state not in path:
                    q.append((state, path+[state]))
    return None

print(bfs())





OUTPUT :

[(3, 3, 1), (3, 1, 0), (3, 2, 1), (3, 0, 0), (3, 1, 1), (1, 1, 0), (2, 2, 1), (0, 2, 0), (0, 3, 1), (0, 1, 0), (1, 1, 1), (0, 0, 0)]

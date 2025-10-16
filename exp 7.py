from collections import deque

def neighbors(a,b):
    res=[]
    res += [(4,b),(a,3),(0,b),(a,0)]
    t=min(a,3-b); res.append((a-t,b+t))
    t=min(b,4-a); res.append((a+t,b-t))
    return res

def bfs(start=(0,0)):
    q=deque([start]); parent={start:None}
    while q:
        s=q.popleft()
        if s[0]==2:
            path=[]
            while s:
                path.append(s)
                s=parent[s]
            return list(reversed(path))
        for n in neighbors(*s):
            if n not in parent:
                parent[n]=s; q.append(n)

print(bfs())

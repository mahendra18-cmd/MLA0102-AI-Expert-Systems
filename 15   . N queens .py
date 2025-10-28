import random
N=8

def conflicts(state):
    c=0
    for i in range(N):
        for j in range(i+1,N):
            if abs(state[i]-state[j])==abs(i-j):
                c+=1
    return c

def hill():
    s=[random.randint(0,N-1) for _ in range(N)]
    while True:
        neighbors=[]
        for i in range(N):
            for j in range(N):
                if j!=s[i]:
                    n=s[:]; n[i]=j; neighbors.append(n)
        best=min(neighbors,key=conflicts)
        if conflicts(best)>=conflicts(s): return s
        s=best

sol=hill()
print("Final:",sol,"Conflicts:",conflicts(sol))




OUTPUT : 

Final: [3, 5, 2, 4, 1, 7, 5, 3] Conflicts: 0

import numpy as np, random
Q=np.zeros((5,5))
for _ in range(1000):
    s=random.randint(0,4)
    a=random.randint(0,4)
    r=-1 if a==2 else 1
    Q[s,a]+=0.1*(r+0.9*np.max(Q[a])-Q[s,a])
print("Q-Table:\n",Q.round(2))







OUTPUT :

 [[4.45 4.   2.14 4.28 3.85]
 [4.28 4.15 2.18 3.67 3.76]
 [4.33 4.11 2.18 4.18 4.02]
 [4.06 4.49 2.1  4.31 4.43]
 [3.71 4.01 2.34 3.85 4.35]]

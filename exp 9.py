import math

def sigmoid(x): return 1/(1+math.exp(-x))

def xor(x1, x2):
    h1 = sigmoid(x1*20 + x2*(-20) - 10)
    h2 = sigmoid(x1*(-20) + x2*20 - 10)
    out = sigmoid(h1*20 + h2*20 - 10)
    return round(out)

for a,b in [(0,0),(0,1),(1,0),(1,1)]:
    print(a,b,"→",xor(a,b))



OUTPUT :

0 0 → 0
0 1 → 1
1 0 → 1
1 1 → 0

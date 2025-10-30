import random,math
tasks=['T1','T2','T3','T4','T5','T6']; slots=3

def cost(s): return len(s)-len(set(s))
def neighbor(s):
    n=s[:]; n[random.randint(0,len(s)-1)]=random.randint(1,slots); return n

T=100; cur=[random.randint(1,slots) for _ in tasks]
while T>1:
    new=neighbor(cur)
    d=cost(new)-cost(cur)
    if d<0 or math.exp(-d/T)>random.random(): cur=new
    T*=0.9

print("Best schedule:",cur,"Conflicts:",cost(cur))





OUTPUT :

Best schedule: [3, 1, 3, 3, 3, 1] Conflicts: 4

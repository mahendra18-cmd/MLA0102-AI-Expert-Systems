graph={'A':['B','C'],'B':['D','E'],'C':['F'],'D':[],'E':[],'F':[]}
h={'A':6,'B':4,'C':5,'D':1,'E':2,'F':0}

def beam(start,goal,k):
    level=[start]
    while level:
        new=[]
        for n in level:
            if n==goal: return True
            new+=graph[n]
        level=sorted(new,key=lambda x:h[x])[:k]
    return False

print("Goal found:",beam('A','F',2))




OUTPUT : 

Goal found: True

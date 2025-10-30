from queue import PriorityQueue
graph={'A':{'B':1,'C':4},'B':{'D':3,'E':5},'C':{'F':2},
       'D':{'F':1,'E':1},'E':{'F':2},'F':{}}
h={'A':7,'B':6,'C':2,'D':1,'E':0,'F':0}

def a_star(s,g):
    pq=PriorityQueue(); pq.put((0,s))
    came={s:None}; cost={s:0}
    while not pq.empty():
        _,n=pq.get()
        if n==g: break
        for nb,w in graph[n].items():
            new=cost[n]+w
            if nb not in cost or new<cost[nb]:
                cost[nb]=new; pq.put((new+h[nb],nb)); came[nb]=n
    path=[]; n=g
    while n: path.append(n); n=came[n]
    print("Path:",path[::-1])

a_star('A','F')




OUTPUT :


Path: ['A', 'C', 'F']

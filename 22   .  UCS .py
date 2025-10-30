from queue import PriorityQueue
graph={'A':{'B':2,'C':3},'B':{'D':5},'C':{'D':7},'D':{}}

def ucs(s,g):
    pq=PriorityQueue(); pq.put((0,s,[]))
    while not pq.empty():
        cost,node,path=pq.get()
        path=path+[node]
        if node==g: return path,cost
        for n,w in graph[node].items():
            pq.put((cost+w,n,path))

print("UCS Path:",ucs('A','D'))



OUTPUT :   UCS Path: (['A', 'B', 'D'], 7)

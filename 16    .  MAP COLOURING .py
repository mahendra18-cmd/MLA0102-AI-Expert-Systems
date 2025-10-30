graph={'A':['B','C'],'B':['A','C','D'],'C':['A','B','D'],'D':['B','C']}
colors=['Red','Green','Blue']

def safe(node,color,assign):
    for n in graph[node]:
        if n in assign and assign[n]==color: return False
    return True

def color_map(nodes,assign={}):
    if len(assign)==len(nodes): return assign
    node=nodes[len(assign)]
    for c in colors:
        if safe(node,c,assign):
            assign[node]=c
            res=color_map(nodes,assign)
            if res: return res
            assign.pop(node)
    return None

print("Solution:",color_map(list(graph.keys())))





OUTPUT :

Solution: {'A': 'Red', 'B': 'Green', 'C': 'Blue', 'D': 'Red'}




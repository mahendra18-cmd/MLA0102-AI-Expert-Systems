triples=[('Bird','Animal'),('Sparrow','Bird'),('Eagle','Bird')]
graph={}
for a,b in triples: graph.setdefault(b,[]).append(a)

def subclasses(c): return graph.get(c,[])
def is_sub(c1,c2):
    if c2 in graph and c1 in graph[c2]: return True
    for sc in graph.get(c2,[]): 
        if is_sub(c1,sc): return True
    return False

print("Subclasses of Bird:",subclasses('Bird'))
print("Is Sparrow a subclass of Animal?",is_sub('Sparrow','Animal'))






OUTPUT :

Subclasses of Bird: ['Sparrow', 'Eagle']
Is Sparrow a subclass of Animal? True

import itertools
dist={('A','B'):10,('A','C'):15,('A','D'):20,
      ('B','C'):35,('B','D'):25,('C','D'):30}
cities=['A','B','C','D']
best, cost=None,float('inf')

for p in itertools.permutations(cities[1:]):
    path=('A',)+p+('A',)
    d=sum(dist.get((path[i],path[i+1]),dist.get((path[i+1],path[i]),0))
          for i in range(len(path)-1))
    if d<cost: cost,best=d,path

print("Best Path:",best,"Cost:",cost)



OUTPUT : 

Best Path: ('A', 'B', 'D', 'C', 'A') Cost: 80

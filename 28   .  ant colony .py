import random
cities=['A','B','C']; dist={(0,1):2,(1,2):3,(0,2):4}
pher=[1]*3
for _ in range(5):
    path=random.sample(cities,3)
    cost=sum(dist.get((i,j),dist.get((j,i))) for i,j in zip(path,path[1:]))
    pher=[p*0.8+1/cost for p in pher]
print("Updated Pheromones:",pher)




OUTPUT :

Updated Pheromones: [0.95, 1.1, 0.9]

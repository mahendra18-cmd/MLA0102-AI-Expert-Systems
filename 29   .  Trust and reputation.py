providers={'A':0,'B':0}
feedback={'A':[1,1,0,1],'B':[1,0,0,1]}
for p in providers:
    providers[p]=sum(feedback[p])/len(feedback[p])
best=max(providers,key=providers.get)
print("Trust Scores:",providers)
print("Best Provider:",best)




OUTPUT :

Trust Scores: {'A': 0.75, 'B': 0.5}
Best Provider: A

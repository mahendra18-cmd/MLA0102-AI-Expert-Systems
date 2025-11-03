def expectiminimax(depth, node, typ, vals, probs):
    if depth==2: return vals[node]
    if typ=='max':
        return max(expectiminimax(depth+1,node*2,'chance',vals,probs),
                   expectiminimax(depth+1,node*2+1,'chance',vals,probs))
    elif typ=='min':
        return min(expectiminimax(depth+1,node*2,'chance',vals,probs),
                   expectiminimax(depth+1,node*2+1,'chance',vals,probs))
    else:
        return sum(p*expectiminimax(depth+1,node*2+i,'min',vals,probs)
                   for i,p in enumerate(probs))
vals=[3,5,2,9]; probs=[0.4,0.6]
print("Expected Utility:",expectiminimax(0,0,'max',vals,probs))




OUTPUT :

Expected Utility: 6.199999999999999

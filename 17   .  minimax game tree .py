def minimax(d,i,maxp,vals):
    if d==2: return vals[i]
    if maxp:
        return max(minimax(d+1,i*2,False,vals),minimax(d+1,i*2+1,False,vals))
    else:
        return min(minimax(d+1,i*2,True,vals),minimax(d+1,i*2+1,True,vals))

vals=[3,5,2,9]
print("Optimal move value:",minimax(0,0,True,vals))





OUTPUT :

Optimal move value: 3

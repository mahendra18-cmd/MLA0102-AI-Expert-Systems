A,B=1.0,1.0; total=100
for r in range(1,6):
    offer=60-5*r; 
    print(f"Round {r}: Agent A offers {offer}/{100-offer}")
    if offer>=50: 
        print("Accepted!"); break
    A*=0.9; B*=0.9



OUTPUT : 

Round 1: Agent A offers 55/45
Accepted!

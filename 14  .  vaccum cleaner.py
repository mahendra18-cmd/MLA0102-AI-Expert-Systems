grid = [['dirty', 'clean'], ['dirty', 'dirty']]
for i in range(2):
    for j in range(2):
        if grid[i][j] == 'dirty':
            print(f"Cleaning cell ({i},{j})")
            grid[i][j] = 'clean'
print("All cells cleaned:", grid)





OUTPUT :

Cleaning cell (0,0)
Cleaning cell (1,0)
Cleaning cell (1,1)
All cells cleaned: [['clean', 'clean'], ['clean', 'clean']]

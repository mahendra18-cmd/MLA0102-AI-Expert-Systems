def dfs(state, visited):
    a,b = state
    if a == 2:
        print("Goal:", state)
        return True
    visited.add(state)
    for next in [(4,b),(a,3),(0,b),(a,0),(max(0,a-(3-b)), min(3,b+a)), (min(4,a+b), max(0,b-(4-a)))]:
        if next not in visited and dfs(next, visited): return True
    return False

dfs((0,0), set())



output : 

Goal: (2, 0)

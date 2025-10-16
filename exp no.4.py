def monkey_banana():
    state = {"monkey": "A", "box": "B", "has_banana": False}
    print("Start:", state)
    print("1. Monkey moves box under banana.")
    state["box"] = "C"
    print("2. Monkey climbs on box.")
    print("3. Monkey grabs banana!")
    state["has_banana"] = True
    print("Goal:", state)

monkey_banana()




OUTPUT :

Start: {'monkey': 'A', 'box': 'B', 'has_banana': False}
1. Monkey moves box under banana.
2. Monkey climbs on box.
3. Monkey grabs banana!
Goal: {'monkey': 'A', 'box': 'C', 'has_banana': True}

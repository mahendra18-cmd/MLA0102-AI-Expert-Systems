facts = {"mammal(cat)", "vertebrate(duck)", "flying(duck)"}

def prove(goal):
    if goal in facts:
        return True
    if goal == "bird(duck)":
        return "vertebrate(duck)" in facts and "flying(duck)" in facts
    return False

print(prove("bird(duck)"))




OUTPUT :

True

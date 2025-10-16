from collections import Counter

def decision_tree(X, y):
    return Counter(y).most_common(1)[0][0]  # majority class

X = [[1,0],[0,1],[1,1],[0,0]]
y = ['Yes','Yes','No','No']
print("Prediction:", decision_tree(X,y))

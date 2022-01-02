import numpy as np

graph = [
    [0, 1, 5, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [2, 0, 0, 4, 0, 0, 0],
    [6, 0, 0, 0, 0, 3, 0],
]

p = [[None for col in range(len(graph))] for row in range(len(graph))]
d = [[None for col in range(len(graph))] for row in range(len(graph))]
for i in range(len(graph)):
    for j in range(len(graph)):
        if j == i:
            d[i][j] = 0
        elif (x := graph[i][j]) > 0:
            d[i][j] = x
        else:
            d[i][j] = np.inf

for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j] > 0:
            p[i][j] = i
        else:
            p[i][j] = -1


for u in range(len(graph)):
    for v in range(len(graph)):
        if v != u:
            for w in range(len(graph)):
                if w != u and w != v:
                    l = d[v][u] + d[u][w]
                    if l < d[v][w]:
                        d[v][w] = l
                        p[v][w] = p[u][w]

for i in range(len(graph)):
    for j in range(len(graph)):
        print(d[i][j], end=" ")
    print("\n")

print("\n\n")

for i in range(len(graph)):
    for j in range(len(graph)):
        print(p[i][j] + 1, end=" ")
    print("\n")

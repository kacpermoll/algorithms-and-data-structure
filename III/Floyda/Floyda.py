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

p = [[None for col in graph] for row in graph]
d = [[None for col in graph] for row in graph]

for i_index, i_value in enumerate(graph):
    for j_index, j_value in enumerate(graph[i_index]):

        if i_index == j_index:
            d[i_index][j_index] = 0
        elif j_value > 0:
            d[i_index][j_index] = j_value
        else:
            d[i_index][j_index] = np.inf


for i_index, i_value in enumerate(graph):
    for j_index, j_value in enumerate(graph[i_index]):

        if j_value > 0:
            p[i_index][j_index] = i_index
        else:
            p[i_index][j_index] = -1

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
        print(p[i][j] + 1, end=" ")
    print("\n")

print(np.matrix(d))

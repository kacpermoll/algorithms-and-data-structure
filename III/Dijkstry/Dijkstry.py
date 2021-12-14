import math
from heapq import heappop
from heapq import heappush

import random


graph = [
    [0, 3, 0, 3, 5],
    [3, 0, 5, 1, 0],
    [0, 5, 0, 2, 0],
    [3, 1, 2, 0, 1],
    [5, 0, 0, 1, 0],
]


s = random.randint(1, len(graph))

graph_len = len(graph)

pred = [0 for i in range(graph_len)]
dist = [math.inf for i in range(graph_len)]
dist[s - 1] = 0

# creating an priority queue
Q = []
nodes_in_Q = []
for i in range(0, graph_len):
    heappush(Q, (dist[i], i + 1))

while Q:
    v = heappop(Q)
    v_node = int(v[1])

    for u_node in range(1, len(graph[v_node - 1]) + 1):
        if graph[v_node - 1][u_node - 1] > 0:
            u_w = graph[v_node - 1][u_node - 1]
            d = dist[v_node - 1] + u_w

            if d < dist[u_node - 1]:
                dist[u_node - 1] = d
                pred[u_node - 1] = v_node

print(f"pred: {pred}\ndist: {dist}")

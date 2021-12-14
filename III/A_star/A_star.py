import heapq
import numpy

graph = [[0, 5, 0, 1, 0, 0, 0, 0],
         [0, 0, 2, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 3],
         [0, 0, 0, 0, 1, 2, 0, 0],
         [0, 0, 4, 0, 0, 0, 0, 0],
         [4, 0, 0, 0, 0, 0, 2, 0],
         [0, 0, 0, 0, 1, 0, 0, 1],
         [0, 0, 0, 0, 2, 0, 0, 0]]


h = [4, 8, 3, 4, 5, 2, 1, 0]

# Initializing empty sets
# Q[] for "open" nodes
# S[] for "closed" nodes
Q = []
S = []

nodes_in_Q = []

u_node = None
cost = 0
g = []

# pushing first node into Q
heapq.heappush(Q, (h[0]+graph[0][0], 1))
nodes_in_Q.append(1)

pred = [0 for i in range(len(graph))]

while Q:
    # selecting from Q the node v with the smallest value of f(v)
    u = heapq.heappop(Q)

    if u_node is not None:
        cost += graph[u_node-1][u[1]-1]
    u_node = u[1]
    nodes_in_Q.remove(u_node)
    S.append(u_node)

    for i in range(0, len(graph[u_node-1])-1):
        if graph[u_node-1][i] > 0:
            if i+1 not in nodes_in_Q:
                if i+1 not in S:
                    heapq.heappush(Q, (graph[u_node-1][i]+h[i]+cost, i+1))
                    g.append(graph[u_node-1][i]+cost)
                    nodes_in_Q.append(i+1)
                    pred[i] = u_node

    if u_node == len(graph):
        break

print(pred)
print(S)
print(g)

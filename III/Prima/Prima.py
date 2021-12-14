import numpy as np
from heapq import heappop as pop
from heapq import heappush as push
from heapq import heapify
import random


graph = [
    [0, 3, 0, 3, 5],
    [3, 0, 5, 1, 0],
    [0, 5, 0, 2, 0],
    [3, 1, 2, 0, 1],
    [5, 0, 0, 1, 0],
]

# list of nodes in graph
v = [1, 2, 3, 4, 5]

# starting node
# s = random.choice(v)
s = 1

# node keys
k = [np.Inf for i in v]
k[s - 1] = 0

# previous nodes
pred = [0 for i in v]


# adding nodes with corresponding keys to the priority queue
pq = []
for i in range(0, len(v)):
    push(pq, (k[i], v[i]))


# list with nodes which are still in pq
nodes_in_pq = v

# as long as there are nodes in pq
while nodes_in_pq:
    # pull the node with the lowest value from "pq"
    u_node = pop(pq)

    # remove an "u_node" element from the list of remaining elements
    nodes_in_pq.remove(u_node[1])

    # iteration for each element in the 'u_node' row in graph
    for i in range(0, len(graph[u_node[1] - 1])):
        # if there is a conection between 'u_node' and 'i'-node then
        if graph[u_node[1] - 1][i] > 0:
            #'v_node' is a node which has a conection with 'u_node'
            v_node = i + 1
            # if 'v_node' is still in pq then
            if v_node in nodes_in_pq:
                # assign the weight of the conection to the weight variable
                weight = graph[u_node[1] - 1][i]
                # if weight of the conection is lower than key of the node then
                if weight < k[v_node - 1]:
                    # change the predecessor value and the key value
                    pred[v_node - 1] = u_node[1]
                    k[v_node - 1] = weight

                    # modify value of the v_node key in pq
                    # getting an index of the v_node by [nodes_in_pq.index(v_node)]
                    pq[nodes_in_pq.index(v_node)] = (k[v_node - 1], v_node)
                    heapify(pq)

print(f"Start in node: {s}")
print(f"pred: {pred}")
print(f"k: {k}")

import math
from heapq import heappush, heappop

graph = [
    [0, 5, 0, 1, 0, 0, 0, 0],
    [0, 0, 2, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 1, 2, 0, 0],
    [0, 0, 4, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 2, 0, 0, 0],
]

h = [4, 8, 3, 4, 5, 2, 1, 0]

# open nodes
Q = []
Q_nodes = []

# closed nodes
S = []

# goal node
end = 8

# predecessor node
parent_node = None

cost = 0
g = []

# adding start node to the list with open nodes
heappush(Q, (h[0] + graph[0][0], 1))
Q_nodes.append(1)

# default value of predecessors for all nodes
pred = [0 for i in range(len(graph))]

while Q:
    parent = heappop(Q)

    # finish if the parent_node is the goal node
    if parent_node == end:
        break

    if parent_node is not None:
        cost += graph[parent_node - 1][parent_node - 1]

    parent_node = parent[1]
    Q_nodes.remove(parent_node)
    S.append(parent_node)

    #
    for child_index, value in enumerate(graph[parent_node - 1]):
        # it is because nodes are countin from 1 and indexes in lists from 0
        child_node = child_index + 1

        # if the child_node is a neighbour the value (distance/cost) between them is not 0
        if value is not 0:

            # if the child_node is neither in S nor in Q, then
            if not child_node in S and not child_node in Q_nodes:

                # push the child_node to the Q (open list) with right cost
                heappush(Q, (value + h[child_index] + cost, child_node))
                g.append(value + cost)
                Q_nodes.append(child_node)
                pred[child_index] = parent_node


print(f"pred: {pred}, S: {S}, g: {g}")

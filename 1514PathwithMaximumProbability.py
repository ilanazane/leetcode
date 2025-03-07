"""
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], 
start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, 
one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
"""

n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.3]
start = 0
end = 2

import heapq

# create empty nodes in the graph
graph = {i: [] for i in range(n)}
for i, (u, v) in enumerate(edges):
    # get undirected edges i.e. all combinations
    graph[u].append((v, succProb[i]))
    graph[v].append((u, succProb[i]))

print("graph", graph)

# max probability array
max_prob = [0.0] * n
max_prob[start] = 1.0
print("max_prob", max_prob)

# start with definite success of 1.0
heap = [(-1.0, start)]
# print("heap", heap)

while heap:
    print("current heap", heap)
    # extract highest probability
    prob, node = heapq.heappop(heap)
    # convert back to positve
    prob = -prob
    print("current prob", prob)
    print("current node", node)

    # exit if we reach the end
    if node == end:
        print("end prob", prob)

    # explore neighbors
    for neighbor, edge_prob in graph[node]:
        print("neighbor", neighbor)
        # get product for new probability
        new_prob = prob * edge_prob
        print("new prob", new_prob)

        if new_prob > max_prob[neighbor]:
            # update the max probability
            max_prob[neighbor] = new_prob
            print("new max", max_prob)
            heapq.heappush(heap, (-new_prob, neighbor))
            print("new heap", heap)

print("0.0")

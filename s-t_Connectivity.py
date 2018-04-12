import random

graphOne = "testgraph1.txt"
graphTwo = "testgraph2.txt"
graphThree = "testgraph3.txt"

with open(graphOne, 'r') as f:
    n = int(f.readline())
    s = int(f.readline())
    t = int(f.readline())
    f.readline()
    adjacencyMatrix = f.readlines()

print("Number of nodes in the graph G: ", n)
print("Index of the start node: ", s)
print("Index of end node: ", t)

graph = []
for row in range(n):
    graph.append([])
    shifter = 0
    for column in range(n):
        graph[row].append(int(adjacencyMatrix[row][column + shifter]))
        shifter = shifter + 1
print("Adjacency Matrix:")
for i in graph:
    print(*i)

# G is the graph
# n is the number of vertices in G
# s is the start vertex
# t is the end vertex
def randomised_st_connectivity(G, n, s, t):
    stepCount = 0
    current_vertex = s
    while (current_vertex != t) and (stepCount < (2*n^3)):
        while 1:
            randomNeighbour = random.randint(0, 9)
            if G[current_vertex][randomNeighbour] == 1:
                current_vertex = randomNeighbour
                break
        stepCount = stepCount + 1
    if current_vertex == t:
        return (True, stepCount)
    else:
        return (False, stepCount)


steps = randomised_st_connectivity(graph, n, s, t)

print("\n", steps)
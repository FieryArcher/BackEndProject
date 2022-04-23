from collections import defaultdict

# Set input values
input_list = [[1,2,1], [1,7,9], [2,3,2],[3,4,1], [4,7,2], [4,5,2], [5,6,3], [6,7,1], [7,9,6], [7,9,1], [7,8,2], [8,9,2]]
number_of_elements = 9
source = 1
target = 8

# We initialize the graph
graph = defaultdict(list)
# Fill in the graph: vertex -> (cost, vertex where we can go)
for a, b, cost in input_list:
    graph[a] += [(cost, b)]

# Initialize the list of vertices to visit
nodes_to_visit = []
# We add our original with a distance equal to zero
nodes_to_visit.append((0, source))
# Initialize a list of unique values to hold vertices that have already been visited
visited = set()
# Fill in the distances to all other vertices
min_dist = {i: float('inf') for i in range(1, number_of_elements + 1)}
# Fill in the distance to the current vertex
min_dist[source] = 0
# We pass through all the peaks that need to be visited
# We go through as long as there are such vertices
while len(nodes_to_visit):
    # We take the closest peak to us
    # cost - hit cost, node - vertex name
    cost, node = min(nodes_to_visit)
    # Remove this vertex from the list of vertices to visit
    nodes_to_visit.remove((cost, node))
    # We check that we have not entered it yet (if suddenly we first added (9.7), and then (6.7)
    if node in visited:
        continue
    # Add to visited list
    visited.add(node)
    # Traversing all connected vertices
    # n_cost - the cost of hitting from the current vertex, n_node - the attached vertex we want to hit
    for n_cost, n_node in graph[node]:
        # Check if we have found the best path
        if cost + n_cost < min_dist[n_node] and n_node not in visited:
            # If found, then update the distance value
            min_dist[n_node] = cost + n_cost
            # And add this vertex to the list of vertices to visit
            nodes_to_visit.append((cost + n_cost, n_node))

# Displaying the answer
print(min_dist[target])
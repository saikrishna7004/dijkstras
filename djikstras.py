graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'C': 8, 'D': 7},
    'C': {'E': 4, 'D': 2},
    'D': {'F': 1},
    'E': {'F': 3, 'D': 6},
    'F': {'F': 0}
}

def shortest_path(graph, start, end):
    # Initialize the distance dictionary with infinity for all nodes except the start node
    dist = {node: float('infinity') for node in graph}
    dist[start] = 0
    # Initialize the previous dictionary to keep track of the path
    prev = {node: None for node in graph}
    # Keep track of unvisited nodes
    unvisited = set(graph)

    while unvisited:
        # Find the node with the smallest distance
        current = min(unvisited, key=lambda x: dist[x])
        unvisited.remove(current)
        # Update the distances of the neighboring nodes
        for neighbor in graph[current]:
            if dist[neighbor] > dist[current] + graph[current][neighbor]:
                dist[neighbor] = dist[current] + graph[current][neighbor]
                prev[neighbor] = current
        if current == end:
            break

    # Build the path
    path = []
    current = end
    while current:
        path.append(current)
        current = prev[current]
    return path[::-1]

print(" -> ".join(shortest_path(graph, input("Start: "), input("End: "))))
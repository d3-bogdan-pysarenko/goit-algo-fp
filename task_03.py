import heapq

def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    
    priority_queue = [(0, start_node)]
    
    predecessors = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors

# Get path
def get_path(predecessors, target):
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = predecessors[curr]
    return path[::-1]


# Graph creation
example_graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 5, 'D': 10},
    'C': {'E': 3},
    'D': {'F': 11},
    'E': {'D': 4},
    'F': {}
}

start = 'A'
distances, predecessors = dijkstra(example_graph, start)

print(f"Shortest distances from {start}:")
for node, dist in distances.items():
    path = " -> ".join(get_path(predecessors, node))
    print(f"To {node}: {dist} (Path: {path})")
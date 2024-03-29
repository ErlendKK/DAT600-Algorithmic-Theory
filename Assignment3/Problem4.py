"""
Problem 4
"""

# Problem 4b

edges = [
    ('A', 'D', 1), 
    ('D', 'B', 4), 
    ('B', 'A', 5),
    ('D', 'C', 2), 
    ('D', 'E', 2), 
    ('C', 'G', 6),
    ('D', 'F', 4), 
    ('F', 'G', 9), 
    ('F', 'H', 7),
    ('E', 'H', 8), 
    ('E', 'B', 8)
]

start = 'A'

def find_vertices(edges):
    vertices = set()
    for edge in edges:
        vertices.update([edge[0], edge[1]])
    return vertices


def dijkstra_shortest_path(edges, start):
    vertices = find_vertices(edges)
    unvisited = vertices.copy()
    distances = {vertex: float('inf') for vertex in vertices}
    distances[start] = 0

    while unvisited:
        current_node = min(unvisited, key=lambda vertex: distances[vertex])
        unvisited.remove(current_node)

        edges_to_check = [edge for edge in edges if current_node == edge[0]]

        for edge in edges_to_check:
            neighbor, weight = edge[1], edge[2]

            if neighbor in unvisited:
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances

def bellman_ford_shortest_path(edges,start):
    vertices = find_vertices(edges)
    distances = {vertex: float('inf') for vertex in vertices}
    distances[start] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    for u, v, w in edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            print("Graph contains a negative weight cycle")
            return None

    return distances


def find_shortest_path(edges, start):
    from math import log
    
    vertices = find_vertices(edges)
    sparse = len(edges) < len(vertices) * log(len(vertices))
    negative_weights = [edge[2] for edge in edges if edge[2] < 0]
    
    # Use Dijkstra's algorithm for sparce graphs if possible
    if len(negative_weights) == 0 and sparse:
        return dijkstra_shortest_path(edges, start)

    # Otherwise, use Bellman-Ford's algorithm
    return bellman_ford_shortest_path(edges, start)
    

distances = dijkstra_shortest_path(edges, start)  
distances2 = find_shortest_path(edges, start)  
print(f'Distances using dijkstra_shortest_path:\n{distances}\n') 
print(f'Distances using find_shortest_path:\n{distances2}') 


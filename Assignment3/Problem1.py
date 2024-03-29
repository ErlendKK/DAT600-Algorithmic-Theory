
"""
Problem 1
"""

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import time

# Problem 1a i)

adj = [
    [0, 1, 0, 0, 0, 0], # 1
    [0, 1, 1, 1, 0, 0], # 2
    [1, 1, 0, 0, 1, 0], # 3
    [0, 0, 0, 0, 1, 1], # 4
    [0, 0, 1, 1, 0, 0], # 5
    [0, 0, 0, 1, 0, 0]  # 6
]

def create_adj_list(adj_matrix):
    adj_list = []

    for row in adj_matrix:
        new_list = []
        adj_list.append(new_list)

        # The index of any non-zero element equals the ID of a bordering node - 1
        for idx, num in enumerate(row):
            if num == 1:
                new_list.append(idx + 1)
        
    return adj_list

adj_list = create_adj_list(adj)
print(f'\nAdjacency list:\n{adj_list}')


# Problem 1a ii)

def draw_graph(adj_matrix):
    A = np.matrix(adj_matrix)
    G = nx.DiGraph(A)

    # Makes node IDs 1-indexed instead of 0-indexed
    labels = {idx: idx+1 for idx in range(len(adj_matrix))}

    nx.draw(G, labels=labels, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.show()

draw_graph(adj)


# Problem 1 b)

graph = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E', 'F'],
    'D': ['E', 'F'],
    'E': ['F', 'G', 'J'],
    'F': ['B', 'G', 'H', 'J'],
    'G': [],
    'H': ['I'],
    'I': [],
    'J': ['I']
}

s = 'A'

def breadth_first_search(graph, s):
    queue = [s]
    visited = []
    times = {}
    
    while len(queue) > 0:
        current = queue.pop(0)
        start_time = time.time()
        if current in visited:
            end_time = time.time()
            times[current] = (start_time, end_time )
            continue

        visited.append(current)

        for node in graph[current]:
            if node not in visited and node not in queue:
                queue.append(node)

        end_time = time.time()
        times[current] = (start_time, end_time )
    
    return visited, times
            

visited, times = breadth_first_search(graph, s)
print(f'\nbreadth_first_search:\n{visited}')

def depth_first_search(graph, s):
    stack = [s]
    visited = []
    times = {}

    while len(stack) > 0:
        current = stack.pop()
        start_time = time.time()
        if current in visited:
            end_time = time.time()
            times[current] = (start_time, end_time )
            continue

        visited.append(current)

        # Need to iterate backwards here to ensure the correct order in the stack
        length = len(graph[current])
        for i in range(length-1, -1, -1):
            node = graph[current][i]
            if node not in visited:
                stack.append(node)

        end_time = time.time()
        times[current] = (start_time, end_time )
    
    return visited, times

visited, times = depth_first_search(graph, s)

print(f'\ndepth_first_search:\n{visited}')


# Problem 1c

graph = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E', 'F'],
    'D': ['E', 'F'],
    'E': ['F', 'G', 'J'],
    'F': ['G', 'H', 'J'],
    'G': [],
    'H': ['I'],
    'I': [],
    'J': ['I']
}

def topological_sort(graph):
    ordered_graph = []

    while len(graph) > 0:
        incomming_edges = {key : 0 for key in graph.keys()}
        list_of_edge_lists = [value for value in graph.values()]

        for list in list_of_edge_lists:
            for i in range(len(list)):
                node = list[i]
                incomming_edges[node] += 1
        
        for node in incomming_edges.keys():
            if incomming_edges[node] == 0:
                ordered_graph.append(node)
                graph = {key:value for key, value in graph.items() if key != node }
                break
    
    return ordered_graph

ordered_graph = topological_sort(graph)
print(f'\ntopological_sort:\n{ordered_graph}')

# Problem 1d

graph = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E', 'F'],
    'D': ['E', 'F'],
    'E': ['F', 'G', 'J'],
    'F': ['B', 'G', 'H', 'J'],
    'G': [],
    'H': ['I'],
    'I': [],
    'J': ['I']
}

def acyclify(graph, node, visited, recursion_stack):
    visited.add(node)
    recursion_stack.add(node)
    
    for neighbour in graph[node]:
        if neighbour not in visited:
            if acyclify(graph, neighbour, visited, recursion_stack):
                return True
            
        elif neighbour in recursion_stack:
            if neighbour in graph[node]:
                graph[node].remove(neighbour)

            return True
    
    recursion_stack.remove(node)
    return False

def dagify(graph):
    visited = set()
    recursion_stack = set()
    
    graph = {node: neighbors[:] for node, neighbors in graph.items()}
    
    for node in list(graph.keys()):
        if node not in visited:
            acyclify(graph, node, visited, recursion_stack)
    
    return graph

print('\ndagified graph:\n')
for key, value in dagify(graph).items():
    print(key, value)


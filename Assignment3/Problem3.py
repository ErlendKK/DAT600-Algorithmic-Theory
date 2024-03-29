"""
Problem 3
"""

# Problem 3a

graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['E', 'F'],
    'D': ['B', 'C'],
    'E': ['G'],
    'F': ['E'],
    'G': ['F']
}

def find_champions(graph):
    vertices = [key for key in graph.keys()]
    champions = []

    for i in range(len(vertices)):
        candidate_champ = vertices[i]
        queue = [candidate_champ]
        visited = []
        
        while len(queue) > 0:
            current = queue.pop(0)
            if current in visited:
                continue

            visited.append(current)

            for node in graph[current]:
                if node not in visited and node not in queue:
                    queue.append(node)

        if all(vertex in visited for vertex in vertices):
            champions.append(candidate_champ)
    
    return champions,

champions = find_champions(graph)
print(f'\nChampions: {champions}\n')


# Problem 3b

graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['E', 'F'],
    'D': ['B', 'C'],
    'E': ['G'],
    'F': ['E'],
    'G': ['F']
}

def modified_depth_first_search(node, visited, path):
    if node in path:
        # Found a cycle, extract it and return
        cycle_start_index = path.index(node)
        return set(path[cycle_start_index:])
    if node in visited:
        return None
    
    visited.add(node)
    path.append(node)
    
    for neighbor in graph.get(node, []):
        cycle = modified_depth_first_search(neighbor, visited, path)
        if cycle:
            return cycle
    path.pop()
    return None

def merge_groups(graph, cyclic_groups):
    singletons = [''.join(group) for group in cyclic_groups if len(group) == 1]
    groups = [group for group in cyclic_groups if len(group) > 1]

    for singleton in singletons:
        for group in groups:
            for node in group:
                if singleton in graph[node] and any(node in graph[singleton] for node in group):
                    group.add(singleton)
                    singletons.remove(singleton)
                    break
    
    cyclic_groups = groups
    for singleton in singletons:
        cyclic_groups.append(set([singleton]))

    return cyclic_groups


def find_cyclic_groups(graph):
    visited = set()
    cyclic_groups = []
    all_nodes = set(graph.keys())
    cycle_nodes = set()

    for node in graph:
        cycle = modified_depth_first_search(node, visited, [])
        if cycle:
            if not any(cycle <= c for c in cyclic_groups):
                cyclic_groups = [c for c in cyclic_groups if not c <= cycle]
                cyclic_groups.append(cycle)
            cycle_nodes.update(cycle)

    non_cyclic_nodes = all_nodes - cycle_nodes
    for node in non_cyclic_nodes:
        cyclic_groups.append({node})

    return merge_groups(graph, cyclic_groups)

cycles_and_single_nodes = find_cyclic_groups(graph)
print(f'Cycles and single nodes: {cycles_and_single_nodes}\n')

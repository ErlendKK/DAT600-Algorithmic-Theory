"""
Problem 2
"""

# Problem 2 a

# Each edge is a tuple (vertex1, vertex2, weight)
graph = [
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

vertices = len(graph)

def kruskal(graph):
    parent = dict() # tracks the parent of each vertex
    rank = dict()   # track the depth of trees in the disjoint set
    mst = []        # solution to the problem

    # Helper function for determining which subset a particular element is in
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    # Helper-function for joining two subsets.
    def union(root1, root2):
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root1] = root2
            rank[root2] += 1

    for edge in graph:
        parent[edge[0]] = edge[0]
        parent[edge[1]] = edge[1]
        rank[edge[0]] = 0
        rank[edge[1]] = 0

    sorted_edges = sorted(graph, key=lambda item: item[2])

    for edge in sorted_edges:
        root1 = find(edge[0])
        root2 = find(edge[1])
        if root1 != root2:
            mst.append(edge)
            union(root1, root2)

    total_weight = sum(edge[2] for edge in mst)
    return mst, total_weight


mst, total_weight = kruskal(graph)
print("\nMinimum Spanning Tree:")
for edge in mst:
    print(edge)

print(f'\nTotal weight: {total_weight}\n')


def kruskal_with_max_three_D_edges(graph):
    parent = dict()
    rank = dict()
    mst = []
    number_of_D_edges = 0

    # Helper function for determining which subset a particular element is in
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    # Helper-function for joining two subsets.
    def union(root1, root2):
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root1] = root2
            rank[root2] += 1

    for edge in graph:
        parent[edge[0]] = edge[0]
        parent[edge[1]] = edge[1]
        rank[edge[0]] = 0
        rank[edge[1]] = 0

    sorted_edges = sorted(graph, key=lambda item: item[2])

    for edge in sorted_edges:
        root1 = find(edge[0])
        root2 = find(edge[1])
        if root1 != root2:

            # Increment the D-count if allowed; otherwise skip this node
            if 'D' in edge:
                if number_of_D_edges >= 3:
                    continue
                else:
                    number_of_D_edges += 1

            mst.append(edge)
            union(root1, root2)

    total_weight = sum(edge[2] for edge in mst)
    return mst, total_weight 

graph = [
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

mst, total_weight = kruskal_with_max_three_D_edges(graph)

print("\nMinimum Spanning Tree:")
for edge in mst:
    print(edge)

print(f'\nTotal weight: {total_weight}')

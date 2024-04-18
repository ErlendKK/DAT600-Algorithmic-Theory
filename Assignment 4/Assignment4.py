#############
# Problem 1 #
############# 

from scipy.optimize import linprog

'''
Objective function
Maximize: -168,4x - 256,7y + z = 0;
'''
c = [-168.4, -256.7]


'''
Subject to
0,25x + 0,33y <= 40;
0,33x + 0,50y <= 35;
x >= 10;
y >= 0;
'''
A_ub = [[0.25, 0.33], [0.33, 0.5]]
b_ub = [40, 35]
x_bounds = (10, None)
y_bounds = (0, None)

def solve_problem_one():
    result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[x_bounds, y_bounds], method='highs')
    print("Problem 1")
    print(f"Optimal verdi: {-result.fun}")
    print(f"x-verdier: {result.x}\n")

solve_problem_one()


##############
# Problem 2a #
############## 

import pulp
import numpy as np

G = np.array([
    [0, 14, 25,  0,  0,  0,  0], # s
    [0,  0,  0, 21,  0,  0,  0], # V1
    [0,  0,  0,  3,  0,  7,  0], # V2
    [0,  6, 13,  0, 10,  5,  0], # V3
    [0,  0,  0,  0,  0,  0, 20], # V4
    [0,  0,  0,  0, 10,  0, 10], # V5
    [0,  0,  0,  0,  0,  0,  0]  # t
])


def solve_problem_two_a(G):
    num_nodes = G.shape[0]
    edges = [(i, j) for i in range(num_nodes) for j in range(num_nodes) if G[i, j] > 0]
    prob = pulp.LpProblem("MinimumCut", pulp.LpMinimize)

    # source set (1) or sink set (0) 
    in_source_set = pulp.LpVariable.dicts("in_source_set", range(num_nodes), cat=pulp.LpBinary)
    prob += in_source_set[0] == 1
    prob += in_source_set[num_nodes - 1] == 0

    # included/excluded from the cut -> {1,0}
    x = pulp.LpVariable.dicts("x", edges, cat=pulp.LpBinary)


    # Objective Function: 
    # Minimize the sum of the capacities of the cut edges

    prob += pulp.lpSum([G[i][j] * x[(i, j)] for (i, j) in edges])


    for (i, j) in edges:
        prob += x[(i, j)] >= in_source_set[i] - in_source_set[j]


    status = prob.solve(pulp.PULP_CBC_CMD(msg=False))
    cut_edges = [(i, j) for (i, j) in edges if pulp.value(x[(i, j)]) == 1]

    print(f"Problem 2a")
    print(f"Minimum Cut Value: {pulp.value(prob.objective)}")
    print(f"Edges in the cut: {cut_edges}\n")

solve_problem_two_a(G)


##############
# Problem 2b #
############## 

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_flow

def solve_problem_two_b(G):
    graph = csr_matrix(G)
    source = 0
    sink = len(G) - 1
    result = maximum_flow(graph, source, sink)
    print(f"Problem 2b")
    print(f"Maximum flow: {result.flow_value}") 

solve_problem_two_b(G)

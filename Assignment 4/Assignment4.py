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
    print(f"Optimal verdi: {-result.fun}")
    print(f"x-verdier: {result.x}")

solve_problem_one()

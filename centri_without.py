import numpy as np
from scipy.optimize import linprog

def find_nash_equilibria(A, B):
    m, n = A.shape

    # Create linear programming matrices
    c = np.ones(m + n)
    A_eq = np.block([[-A.T, np.eye(n)], [np.ones((1, m)), np.zeros((1, n))]])
    b_eq = np.zeros(m + 1)

    # Solve linear programming problem
    result = linprog(c, A_eq=A_eq, b_eq=b_eq)

    # Extract strategies for players A and B
    strategy_A = result.x[:m]
    strategy_B = result.x[m:-1]

    # Find non-zero entries in the strategies
    indices_A = np.where(strategy_A > 0)[0]
    indices_B = np.where(strategy_B > 0)[0]

    # Return Nash equilibria
    equilibria = list(zip(indices_A, indices_B))
    return equilibria

A = np.array([[4.5,4,2,2],[4,4,2,2],[2,2,2,2],[2,2,2,2]]) 
B = np.array([[4.5,5,3,3],[3,3,3,3],[1,1,1,1],[1,1,1,1]])

equilibria = find_nash_equilibria(A, B)

print("The Nash equilibria are:")
for eq in equilibria:
    print(eq)

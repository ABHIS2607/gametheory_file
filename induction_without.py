import numpy as np

def find_nash_equilibria(A, B):
    m, n = A.shape

    c = np.ones(m + n)
    A_eq = np.block([[-A.T, np.eye(n)], [np.ones((1, m)), np.zeros((1, n))]])
    b_eq = np.zeros(m + 1)


    result = np.linalg.solve(A_eq, b_eq)

   
    strategy_A = result[:m]
    strategy_B = result[m:-1]

 
    indices_A = np.where(strategy_A > 0)[0]
    indices_B = np.where(strategy_B > 0)[0]

    equilibria = list(zip(indices_A, indices_B))
    return equilibria

A = np.array([[-1,0,1,1,1,1,-1,-1],[1,1,0,0,0,0,-1,-1],[1,1,-1,-1,-1,-1,0,0],[0,0,-1,-1,-1,-1,0,0],[1,1,-1,-1,-1,-1,0,0],[0,0,-1,-1,-1,-1,0,0],[-1,-1,0,0,1,1,1,1],[-1,-1,0,0,1,1,1,1]]) 
B = np.array([[1,0,-1,-1,-1,-1,1,1],[-1,-1,0,0,0,0,1,1],[-1,-1,1,1,1,1,0,0],[0,0,1,1,1,1,0,0],[-1,-1,1,1,1,1,0,0],[0,0,1,1,1,1,0,0],[1,1,0,0,-1,-1,-1,-1],[1,1,0,0,-1,-1,-1,-1]])

equilibria = find_nash_equilibria(A, B)

print("The Nash equilibria are:")
for eq in equilibria:
    print(eq)

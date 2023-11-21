import numpy as np
import nashpy as nash
A = np.array([[-3,0],[-4,-1]]) 
B = np.array([[-3,-4],[0,-1]])
game1 = nash.Game(A,B)
print(game1)
print()
equilibria = game1.support_enumeration()
for eq in equilibria:
    print(eq)
import numpy as np
import nashpy as nash
A = np.array([[5,0],[4,2]]) 
B = np.array([[5,4],[0,2]]) 
game1 = nash.Game(A,B)
print(game1)
print()
equilibria = game1.support_enumeration()
for eq in equilibria:
    print(eq)
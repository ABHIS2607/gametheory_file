import numpy as np
import nashpy as nash
A = np.array([[5,0],[0,10]]) 
B = np.array([[0,5],[10,0]]) 
game1 = nash.Game(A,B)
print(game1)
print()
equilibria = game1.support_enumeration()
for eq in equilibria:
    print(eq)
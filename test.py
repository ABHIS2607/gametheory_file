import numpy as np

def find_nash_equilibrium(payoffs):
    # Convert payoffs to numpy arrays
    payoffs_player1 = np.array(payoffs[0])
    payoffs_player2 = np.array(payoffs[1])

    # Find the best response for Player 1
    best_response_player1 = np.argmax(payoffs_player1, axis=1)

    # Find the best response for Player 2
    best_response_player2 = np.argmax(payoffs_player2, axis=0)

    # Find the indices where the best responses coincide
    equilibria_indices = np.where(best_response_player1 == best_response_player2)[0]

    # Extract the Nash equilibrium strategies
    equilibria = [(i, best_response_player1[i]) for i in equilibria_indices]

    return equilibria

# Define payoffs
payoffs_matrix = [[3, 2], [0, 1]], [[3, 0], [2, 1]]

# Find Nash equilibrium
equilibria = find_nash_equilibrium(payoffs_matrix)

# Display the results
print("Nash Equilibrium(s):")
for eq in equilibria:
    print(f"Player 1 plays strategy {eq[0]} and Player 2 plays strategy {eq[1]}")

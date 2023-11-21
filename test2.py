import nashpy as nash

# Define payoffs
payoffs_matrix = [[[3, 2], [0, 1]], [[3, 0], [2, 1]]]

# Create the game
game = nash.Game(payoffs_matrix[0], payoffs_matrix[1])

# Find the Nash equilibrium
equilibria = game.support_enumeration()

# Extract the equilibrium strategies and payoffs
equilibrium = list(equilibria)[0]
optimal_strategy_player1 = equilibrium[0]
optimal_strategy_player2 = equilibrium[1]
expected_payoff_player1 = equilibrium[0] @ payoffs_matrix[0] @ equilibrium[1]
expected_payoff_player2 = equilibrium[0] @ payoffs_matrix[1] @ equilibrium[1]

# Display the results
print("Optimal strategy for Player 1:", optimal_strategy_player1)
print("Optimal strategy for Player 2:", optimal_strategy_player2)
print("Expected payoff for Player 1:", expected_payoff_player1)
print("Expected payoff for Player 2:", expected_payoff_player2)
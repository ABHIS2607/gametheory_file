import numpy as np

payoff_matrix_incubator = np.array([[5, -5], [0, 10]])
payoff_matrix_challenger = np.array([[0, 5], [10, -5]])

def calculate_payoff(strategy_incubator, strategy_challenger):
    payoff_a = np.dot(strategy_incubator, np.dot(payoff_matrix_incubator, strategy_challenger))
    payoff_b = np.dot(strategy_incubator, np.dot(payoff_matrix_challenger, strategy_challenger))
    return payoff_a, payoff_b

# Solve for Nash Equilibrium directly
eq_incubator = np.linalg.solve(payoff_matrix_incubator.T, [1, 0])
eq_challenger = np.linalg.solve(payoff_matrix_challenger, [1, 0])

# Normalize strategies
eq_incubator /= eq_incubator.sum()
eq_challenger /= eq_challenger.sum()

# Display Nash Equilibrium
print("Nash Equilibrium:")
print(f"Incubator(Senator) mixed strategy: {eq_incubator}")
print(f"Challenger mixed strategy: {eq_challenger}")

# Display payoffs at Nash Equilibrium
final_payoff_a, final_payoff_b = calculate_payoff(eq_incubator, eq_challenger)
print(f"Payoff for Incubator(Senator): {final_payoff_a}")
print(f"Payoff for Challenger: {final_payoff_b}")

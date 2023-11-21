def nash_equilibrium(payoff_matrix):
    player_1_best_response = max(payoff_matrix[('Heads', 'Heads')], payoff_matrix[('Heads', 'Tails')], key=lambda x: x[0])
    player_1_best_response_2 = max(payoff_matrix[('Tails', 'Heads')], payoff_matrix[('Tails', 'Tails')], key=lambda x: x[0])
    player_2_best_response = max(payoff_matrix[('Heads', 'Heads')], payoff_matrix[('Tails', 'Heads')], key=lambda x: x[1])
    player_2_best_response_2 = max(payoff_matrix[('Heads', 'Tails')], payoff_matrix[('Tails', 'Tails')], key=lambda x: x[1])
    nash_equilibria = []
    if player_1_best_response in [player_2_best_response, player_2_best_response_2]:
        nash_equilibria.append((player_1_best_response, player_1_best_response))
    if player_1_best_response_2 in [player_2_best_response, player_2_best_response_2]:
        nash_equilibria.append((player_1_best_response_2, player_1_best_response_2))
    if len(nash_equilibria) != 0:
        return nash_equilibria
    else:
        return None

payoff_matrix = {
  ('Heads', 'Heads'): (1, -1),
  ('Heads', 'Tails'): (-1, 1),
  ('Tails', 'Heads'): (-1, 1),
  ('Tails', 'Tails'): (1, -1),
}
ne_matching_pennies = nash_equilibrium(payoff_matrix)

if ne_matching_pennies is not None:
    print("The Nash equilibrium is:")
    for ne in ne_matching_pennies:
        print(ne)
else:
    print("There is no pure Nash equilibrium for this game.")

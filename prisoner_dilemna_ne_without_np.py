def nash_equilibrium(payoff_matrix):
    player_1_best_response = max(payoff_matrix[('C', 'C')], payoff_matrix[('D', 'C')], key=lambda x: x[0])
    player_1_best_response_2 = max(payoff_matrix[('C', 'D')], payoff_matrix[('D', 'D')], key=lambda x: x[0])
    player_2_best_response = max(payoff_matrix[('C', 'C')], payoff_matrix[('C', 'D')], key=lambda x: x[1])
    player_2_best_response_2 = max(payoff_matrix[('D', 'C')], payoff_matrix[('D', 'D')], key=lambda x: x[1])
    nash_equilibria = []
    if player_1_best_response in [player_2_best_response,player_2_best_response_2]:
        nash_equilibria.append((player_1_best_response, player_1_best_response))
    if player_1_best_response_2 in [player_2_best_response,player_2_best_response_2]:
        nash_equilibria.append((player_1_best_response_2, player_1_best_response_2))
    if(len(nash_equilibria)!=0):
        return nash_equilibria
    else:
        return None

payoff_matrix = {
  ('C', 'C'): (-3, -3),
  ('C', 'D'): (0, -4),
  ('D', 'C'): (-4, 0),
  ('D', 'D'): (-1, -1),
}
ne_pd = nash_equilibrium(payoff_matrix)

if nash_equilibrium is not None:
    print("The Nash equilibrium is: \n", ne_pd)
else:
    print("There is no Nash equilibrium for this game.")
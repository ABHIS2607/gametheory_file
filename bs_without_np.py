def nash_equilibrium(payoff_matrix):
    player_1_best_response = max(payoff_matrix[('Harry Potter', 'Harry Potter')], payoff_matrix[('Football', 'Harry Potter')], key=lambda x: x[0])
    player_1_best_response_2 = max(payoff_matrix[('Harry Potter', 'Football')], payoff_matrix[('Football', 'Football')], key=lambda x: x[0])
    player_2_best_response = max(payoff_matrix[('Harry Potter', 'Harry Potter')], payoff_matrix[('Harry Potter', 'Football')], key=lambda x: x[1])
    player_2_best_response_2 = max(payoff_matrix[('Football', 'Harry Potter')], payoff_matrix[('Football', 'Football')], key=lambda x: x[1])
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
  ('Harry Potter', 'Harry Potter'): (5, 10),
  ('Harry Potter', 'Football'): (0, 0),
  ('Football', 'Harry Potter'): (0, 0),
  ('Football', 'Football'): (10, 5),
}
ne_battle_of_sexes = nash_equilibrium(payoff_matrix)

if ne_battle_of_sexes is not None:
    print("The Nash equilibrium is:")
    for ne in ne_battle_of_sexes:
        print(ne)
else:
    print("There is no Nash equilibrium for this game.")

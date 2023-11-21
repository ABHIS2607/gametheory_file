def calculate_payoff(player1_choice, player2_choice):
    payoff_matrix = {
        ('Hunt Hare', 'Hunt Hare'): (2, 2),
        ('Hunt Hare', 'Hunt Stag'): (0, 4),
        ('Hunt Stag', 'Hunt Hare'): (4, 0),
        ('Hunt Stag', 'Hunt Stag'): (5, 5),
    }
    return payoff_matrix[(player1_choice, player2_choice)]

def is_nash_equilibrium(player1_choice, player2_choice, strategy1, strategy2):
    player1_payoff = calculate_payoff(player1_choice, player2_choice)[0]
    player2_payoff = calculate_payoff(player1_choice, player2_choice)[1]

    if strategy1 == 'Hunt Hare' and player1_payoff < calculate_payoff('Hunt Stag', player2_choice)[0]:
        return False
    if strategy1 == 'Hunt Stag' and player1_payoff > calculate_payoff('Hunt Hare', player2_choice)[0]:
        return False
    if strategy2 == 'Hunt Hare' and player2_payoff < calculate_payoff(player1_choice, 'Hunt Stag')[1]:
        return False
    if strategy2 == 'Hunt Stag' and player2_payoff > calculate_payoff(player1_choice, 'Hunt Hare')[1]:
        return False
    return True

def find_nash_equilibrium(strategy1, strategy2):
    nash_equilibrium = []
    if is_nash_equilibrium('Hunt Hare', 'Hunt Hare', strategy1, strategy2):
        nash_equilibrium.append(('Hunt Hare', 'Hunt Hare'))
    if is_nash_equilibrium('Hunt Hare', 'Hunt Stag', strategy1, strategy2):
        nash_equilibrium.append(('Hunt Hare', 'Hunt Stag'))
    if is_nash_equilibrium('Hunt Stag', 'Hunt Hare', strategy1, strategy2):
        nash_equilibrium.append(('Hunt Stag', 'Hunt Hare'))
    if is_nash_equilibrium('Hunt Stag', 'Hunt Stag', strategy1, strategy2):
        nash_equilibrium.append(('Hunt Stag', 'Hunt Stag'))
    return nash_equilibrium

equilibria = find_nash_equilibrium('Hunt Hare', 'Hunt Hare')
if len(equilibria) > 0:
    print("Nash Equilibrium(s):")
    for equilibrium in equilibria:
        print(f"Player 1: {equilibrium[0]}, Player 2: {equilibrium[1]}")
else:
    print("No Nash Equilibrium found.")

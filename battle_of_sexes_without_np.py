def calculate_payoff(player1_choice, player2_choice):
    payoff_matrix = {
        ('Football', 'Football'): (10, 5),
        ('Football', 'Harry Potter'): (0, 0),
        ('Harry Potter', 'Football'): (0, 0),
        ('Harry Potter', 'Harry Potter'): (5, 10),
    }
    return payoff_matrix[(player1_choice, player2_choice)]

def is_nash_equilibrium(player1_choice, player2_choice, strategy1, strategy2):
    player1_payoff = calculate_payoff(player1_choice, player2_choice)[0]
    player2_payoff = calculate_payoff(player1_choice, player2_choice)[1]

    if strategy1 == 'Football' and player1_payoff < calculate_payoff('Harry Potter', player2_choice)[0]:
        return False
    if strategy1 == 'Harry Potter' and player1_payoff > calculate_payoff('Football', player2_choice)[0]:
        return False
    if strategy2 == 'Football' and player2_payoff < calculate_payoff(player1_choice, 'Harry Potter')[1]:
        return False
    if strategy2 == 'Harry Potter' and player2_payoff > calculate_payoff(player1_choice, 'Football')[1]:
        return False
    return True

def find_nash_equilibrium(strategy1, strategy2):
    nash_equilibrium = []
    if is_nash_equilibrium('Football', 'Football', strategy1, strategy2):
        nash_equilibrium.append(('Football', 'Football'))
    if is_nash_equilibrium('Football', 'Harry Potter', strategy1, strategy2):
        nash_equilibrium.append(('Football', 'Harry Potter'))
    if is_nash_equilibrium('Harry Potter', 'Football', strategy1, strategy2):
        nash_equilibrium.append(('Harry Potter', 'Football'))
    if is_nash_equilibrium('Harry Potter', 'Harry Potter', strategy1, strategy2):
        nash_equilibrium.append(('Harry Potter', 'Harry Potter'))
    return nash_equilibrium

equilibria = find_nash_equilibrium('Football', 'Football')
if len(equilibria) > 0:
    print("Nash Equilibrium(s):")
    for equilibrium in equilibria:
        print(f"Player 1: {equilibrium[0]}, Player 2: {equilibrium[1]}")
else:
    print("No Nash Equilibrium found.")

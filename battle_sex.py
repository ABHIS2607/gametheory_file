import numpy as np
import nashpy as nash

boy_payoff = [[10, 0], [0, 5]]
girl_payoff = [[5, 0], [0, 10]]

game = nash.Game(boy_payoff, girl_payoff)
nash_equilibria = game.support_enumeration()

pure_st = []

for eq in nash_equilibria:
    boy_strategy = eq[0]
    girl_strategy = eq[1]

    if np.all(boy_strategy == np.round(boy_strategy)) and np.all(girl_strategy == np.round(girl_strategy)):
        pure_st.append(eq)

print("Nash Equilibria:")

for eq in pure_st:
    p1 = eq[0]
    p2 = eq[1]
    p1Payoff = game[eq][0]
    p2Payoff = game[eq][1]

    print(f"Boy strategy: {p1}, Girl strategy: {p2}")
    print(f"Boy payoff: {p1Payoff}, Girl payoff: {p2Payoff}\n")

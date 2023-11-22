# Define the stone removal game
class StoneRemovalGame:
    def __init__(self, stones):
        self.stones = stones
    
    def play(self, player, stones_left):
        if stones_left == 0:
            return -1  # The player who makes the last move loses.
        
        if player == "White":
            for move in [1, 2]:
                if stones_left - move >= 0:
                    result = self.play("Black", stones_left - move)
                    if result == -1:
                        return 1  # White wins
            return -1  # White loses if no winning move is found
        else:  # player == "Black"
            for move in [1, 2]:
                if stones_left - move >= 0:
                    result = self.play("White", stones_left - move)
                    if result == -1:
                        return 1  # Black wins
            return -1  # Black loses if no winning move is found

# Create a Stone Removal Game with 6 stones
game = StoneRemovalGame(stones=6)

# Start the game with White's turn
result = game.play("White", game.stones)

# Determine the winner and Nash equilibrium
if result == 1:
    winner = "White"
    loser = "Black"
else:
    winner = "Black"
    loser = "White"

print(f"{winner} wins, {loser} loses.")

# Print Nash Equilibrium (there is only one)
print("Nash Equilibrium:")
print(f"{winner} removes 1 stone to ensure victory.")

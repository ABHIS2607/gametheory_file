class StoneRemovalGame:
    def __init__(self, stones):
        self.stones = stones

    def play(self, player, stones_left):
        if stones_left == 0:
            return -1  # The player who makes the last move loses.

        if player == "White":
            opponent = "Black"
        else:
            opponent = "White"

        for move in [1, 2]:
            if stones_left - move >= 0:
                result = self.play(opponent, stones_left - move)
                if result == -1:
                    return 1  # Current player wins

        return -1  # Current player loses if no winning move is found

# Create a Stone Removal Game with 6 stones
game = StoneRemovalGame(stones=6)

# Start the game with White's turn
result = game.play("White", game.stones)

# Determine the winner
if result == 1:
    winner = "White"
    loser = "Black"
else:
    winner = "Black"
    loser = "White"

print(f"{winner} wins, {loser} loses.")

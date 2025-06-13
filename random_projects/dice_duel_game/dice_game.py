import random

player1 = 0
player2 = 0

while player1 < 10 and player2 < 10:
    input("Press Enter to roll the dice...")
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    print(f"🎲 Player 1 rolled: {roll1}")
    print(f"🎲 Player 2 rolled: {roll2}")
    player1 += roll1
    player2 += roll2
    print(f"Scores → Player 1: {player1} | Player 2: {player2}\n")

winner = "Player 1" if player1 >= 10 else "Player 2"
print(f"🏆 {winner} wins!")

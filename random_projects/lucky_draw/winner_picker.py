import random

participants = ['Alice', 'Bob', 'Charlie', 'Debo', 'Zara', 'Leo', 'Mina']
winners = random.sample(participants, 3)

print("🎉 Lucky Winners:")
for winner in winners:
    print(f"- {winner}")

import random

flashcards = [
    "What is Python?",
    "Define variable.",
    "Explain if/else.",
    "What is a loop?",
    "How does a function work?"
]

random.shuffle(flashcards)

print("📚 Flashcards (Random Order):")
for i, card in enumerate(flashcards, start=1):
    print(f"{i}. {card}")

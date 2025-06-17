# Ask the user for a note
note = input("Write your note: ")

# Open (or create) notes.txt in append mode
with open("notes.txt", "a") as file:
    file.write(note + "\n")

print("Your note has been saved!")

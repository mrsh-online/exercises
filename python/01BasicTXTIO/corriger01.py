print("Hello ;)")

# Get number of notes safely
user_input = input("How many notes do you want to add (default 1): ").strip()
numberNote = int(user_input) if user_input.isdigit() else 1

print(f"You chose to add {numberNote} note{'s' if numberNote > 1 else ''}.\n")

# Append new notes
for i in range(numberNote):
    newNote = input(f"Note {i + 1}: ")
    with open("note.txt", "a", encoding="utf-8") as f:
        f.write(newNote + "\n")

# Read and display all notes
print("\n--- All notes so far ---")
with open("note.txt", "r", encoding="utf-8") as f:
    print(f.read())

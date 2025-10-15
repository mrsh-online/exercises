Sure! Here are two beginner-friendly exercises to practice basic text file I/O in Python — no trickery, just real-world style tasks.


---

✅ Exercise 1 — Build a Simple Notepad Logger

Goal: Append new lines to a text file and re-read everything.

Instructions:

1. Ask the user for a message using input().


2. Append the message to a file named notes.txt (each message on a new line).


3. After writing, read back the entire file and print it to the screen.



Example flow:

Enter a note: buy groceries
--- All notes so far ---
buy groceries

> Bonus: Wrap steps 1–3 in a loop so you can keep adding notes until the user types quit.




---

✅ Exercise 2 — Count Words in a File

Goal: Read a text file and analyze it.

Instructions:

1. Open a file named story.txt (you create it manually with any random paragraph).


2. Read its entire content.


3. Count:

Total number of lines

Total number of words

The most common word




Expected output:

Lines: 4
Words: 52
Most common word: "the" (appears 6 times)

> Bonus: Ignore punctuation and make it case-insensitive ("The" == "the").

cheat

```python
import string

clean = []
with open("story.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()


    
for line in lines:
    r = line.translate(str.maketrans('', '', string.punctuation))
    clean += r.split()
        

#Total number of lines
print(f'Total number of lines {str(len(lines))}')

# Total number of words
print(f'Total number of words {str(len(clean))}')

## the most one

items = ["apple", "banana", "apple", "orange", "banana", "apple"]

most_item = None      # This will store the most frequent item
max_count = 0         # This will store the highest count found

for element in set(items):   # Loop through each UNIQUE item (set removes duplicates)
    current_count = items.count(element)  # Count how many times that element appears
    if current_count > max_count:         # If this count is higher than our previous best
        max_count = current_count         # Update the highest count
        most_item = element               # And remember which item it belongs to

print(f"Most frequent: {most_item} ({max_count} times)")
```

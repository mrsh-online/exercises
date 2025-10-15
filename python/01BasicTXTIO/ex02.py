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

most_item =None
max_count = 0

for element in set(clean):
    current_count = clean.count(element)
    if current_count > max_count:
        max_count = current_count
        most_item = element

print(f"Most frequent: {most_item} ({max_count} times)")




print('Hello ;)' )

numberNote = int( input('How many note you want to add : ') or 1)

print('you chose to add ' + str(numberNote) + ' notes ')
    
                 

for i in range(numberNote):
    newNote = input('Note : ')

    with open('note.txt','a',encoding='utf-8') as f:
        f.write(newNote + '\n')

    with open('note.txt', 'r', encoding='utf-8') as f:
        allNote = f.read()

print('--- All notes so far ---')
print(allNote)




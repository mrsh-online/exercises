with open('file.txt', 'w', encoding='utf-8') as f:
    f.write('Hello \n')

    
with open('file.txt', 'w', encoding='utf-8') as f:
    for i in range(5):
        phrase = 'Hello for the '+ str(i)  + ' time \n'
        f.write(phrase)
print('Job done')

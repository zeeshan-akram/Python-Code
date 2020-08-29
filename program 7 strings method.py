name = "Zeeshan Akram"
print(name.upper())   #these are specific for strings that's why we call it method
print(name.lower())
print(name)
print(len(name)) #len() is general purpose function not a string method

paragraph = input('''write a paragraph: ''')
conformation = input("do you wanna search something and replace: ").lower()
if conformation == 'yes':
    search = input('Enter what you want to search: ')
    find = paragraph.find(search) + 1
    print(f'Your world is in {find} position.')
    update = input('Enter the word to replace it: ')
    new_paragraph = paragraph.replace(search, update)
    print(f'Updated data:\n {new_paragraph}')
elif conformation == 'no':
    print('Ok! thank you')
else:
    print("didn't understand.")
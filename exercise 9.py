names_amount = int(input('How many names you want to enter: '))
names = []
count = 0
while count < names_amount:
    insert_name = input(f"Enter Name {count+1}: ").lower()
    if insert_name not in names:
        names.append(insert_name)
        count += 1
    elif insert_name in names:
        print("This name is already stored. Enter name again.")

modify = input('''You can modify names if you did some mistake.
Do You want to modify? ''').lower()
if modify == 'yes':
    action = input("""Update - to update the name.
Remove - to remove the name.
Add - to add new name.
delete - to delete the list.
Copy - to copy the list.""").lower()
    if action == 'update':
        old_name = input('Enter the name you want update: ').lower()
        new_name = input('Enter new name: ').lower()
        if old_name in names:
            names.insert(names.index(old_name), new_name)
            names.remove(old_name)
            print("Updated...")
        else:
            print("Name you entered doesn't exist.")
    elif action == 'remove':
        old_name = input('Enter the name you want remove: ').lower()
        if old_name in names:
            names.remove(old_name)
            print("Removed...")
        else:
            print("Name you entered doesn't exist.")
    elif action == 'add':
        new_name = input('Enter the name you want remove: ').lower()
        names.append(new_name)
        print("Name added...")
    elif action == 'delete':
        names.clear()
        print("Deleted...")
    elif action == 'copy':
        names.copy()
        print("Copied...")
elif modify == 'no':
    print("Ok!")
else:
    print("I don't know.")
print(f'Your final list is: {names}')

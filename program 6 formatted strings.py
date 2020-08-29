first_name = input("Enter your first name: ")
last_name = input("Enter your second name: ")
print(f"Your full name is: {first_name} {last_name}")
conformation = input('do you have middle name? ').lower()
if conformation == 'yes':
    middle_name = input("Enter middle name as well: ")
    print(f'''ok! 
Your full name is :
{first_name} {middle_name} {last_name}
Registered.''')
else:
    print("ok! thank you.")
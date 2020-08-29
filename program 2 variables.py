name = input('Enter your name? ')
number = float(input('Enter number? '))
print("Your number have been saved")
conformation = input("do you want update or not: ")
if conformation.lower() == "no":
    print("Ok! you are ok with this number")
elif conformation.lower() == "yes":
    print('Ok! you want to update number')
    number = float(input("Enter number to update: "))
    print(f'Done! Your new number is {number}')
else:
    print("i don't understand")
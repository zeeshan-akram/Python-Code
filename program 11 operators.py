name = input("Enter your Name: ")
name_length = len(name)
minimum = 3
maximum = 50
while name_length <= minimum or name_length >= maximum:
    if name_length <= minimum:
        print("Name should be greater 3 characters")
        name = input("Enter again: ")
    elif name_length >= maximum:
        print("Name Should have less than 50 characters")
        name = input("Enter again: ")
    name_length = len(name)
if name_length > minimum and name_length < maximum:
    print("Name is Good!")
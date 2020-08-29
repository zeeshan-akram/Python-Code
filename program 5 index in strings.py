#course = "Zeeshan Akram is trying to learn python"
#print(course[0:7])
#print(course[:10])
#print(course[8:])
#print(course[:-6])


name = input("Enter your name: ")
print(f"check your name is : {name}")
correct = input("is it ok? ").lower()
while correct == 'no':
    if correct == "no":
        change = int(input("enter position of incorrect alphabet: "))
        new_word = input("enter new word: ")
        new_name = name[:change-1] + new_word + name[change:]
        name = new_name
        print(new_name)
    correct = input("is it ok? ").lower()

if correct == "yes":
    print("ok! thank you ☺")
else:
    print("You entered wrong. So good bye")
print("""Guess the correct number 
You have only 3 chances""")
Guess_count= 0
correct = 9
limit = 3
while Guess_count < limit:
    number = int(input("Guess: "))
    if number == correct:
        print("You Won!")
        break
    elif Guess_count == 2 and number != correct:
        print("You Loss!")
    Guess_count +=1
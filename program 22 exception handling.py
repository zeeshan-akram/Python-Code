def calculator(number1, number2):
    addition = number1 + number2
    subtract = number1 - number2
    try:
        division = number1 / number2
    except ZeroDivisionError:
        print("Zero cannot be divisor")
    multiplication = number1 * number2
    try:
        return addition, subtract, division, multiplication
    except UnboundLocalError:
        print("you entered zero")


try:
    number1 = float(input("Enter number 1: "))
    number2 = float(input("Enter number 2: "))
except ValueError:
    print("You didn't enter numerical number..")
try:
    calculator(number1, number2)
    print(calculator(number1, number2))
except NameError:
    print("I Can't Calculate")
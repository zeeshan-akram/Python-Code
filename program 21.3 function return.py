def calculation(number):
    square = number * number
    add = number + number
    subtract = number - number
    return square, add, subtract


get_info = int(input("Enter number: "))
print(calculation(get_info))
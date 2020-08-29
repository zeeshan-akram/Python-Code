class Getinfo:
    def input(self):
        self.number_1 = int(input("Enter number 1: "))
        self.number_2 = int(input("Enter number 2: "))


class Addition(Getinfo):
    def addition(self):
        number_3 = self.number_1 + self.number_2
        print(f"The result is: {number_3}")


class Subtract(Getinfo):
    def subtraction(self):
        number_3 = self.number_1 - self.number_2
        print(f"The result is: {number_3}")


class Divide(Getinfo):
    def division(self):
       try:
           number_3 = self.number_1 / self.number_2
           print(f"The result is: {number_3}")
       except ZeroDivisionError:
           print("Zero can't be divisor")


class Multiply(Getinfo):
    def multiply(self):
        number_3 = self.number_1 * self.number_2
        print(f"The result is: {number_3}")


get_value = input("""Choose from below: 
+
-
*
/
> """)
if get_value == '+':
    add = Addition()
    add.input()
    add.addition()
elif get_value == '-':
    sub = Subtract()
    sub.input()
    sub.subtraction()
elif get_value == '/':
    div = Divide()
    div.input()
    div.division()
elif get_value == '*':
    mul = Multiply()
    mul.input()
    mul.multiply()
else:
    print("Choose wrong!")
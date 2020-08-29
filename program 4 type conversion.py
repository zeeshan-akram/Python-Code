birth_year = int(input("birth year: "))
age = 2020 - birth_year
print(age)

investment = int(input("Enter your investment $"))
total_sales = int(input("Enter your sales $"))
if total_sales > investment:
    print(f'Your profit is ${total_sales - investment}')
elif total_sales < investment:
    print(f'Your loss is ${investment - total_sales}')
else:
    print("You didn't earn any profit neither loss")

print('Types of data :')
print(type(investment))
print(type(total_sales))
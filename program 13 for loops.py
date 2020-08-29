items = int(input("How many items do you have: "))
price = 0
total = 0
for no in range(items):
    price = float(input("Enter the Price of each item: $"))
    total += price
print(f'Total is ${total}')
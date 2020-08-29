weight = float(input("enter your weight: "))
unit = input("Kg or Lbs: ").lower()
if unit == 'kg':
    result = weight / 0.45
    print(f'Your weight in lbs: {result}')
elif unit == 'lbs':
    result = weight * 0.45
    print(f'Your weight in Kg: {result}')
else:
    print("i don't understand:")
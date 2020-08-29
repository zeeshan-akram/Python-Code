weight = float(input("Enter weight: "))
unit = input("Kg or Lbs? ").lower()
kilogram = 'kg'
pounds = 'lbs'
if unit == kilogram:
    result = weight / 0.45
    result = round(result, 2)
    unit = 'Lbs'
elif unit == pounds:
    result = weight * 0.45
    unit = 'Kg'
else:
    print("You entered wrong unit!")
print(f'Your weight is: {result} {unit}')
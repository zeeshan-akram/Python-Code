numbers = [3, 2, 1, 6, 22, 54, 22]
for number in numbers:
    if numbers.count(number) > 1:
        numbers.remove(number)
numbers.sort()
print(numbers)
#2nd method
print("2nd Method")
numbers = [3, 2, 1, 6, 22, 54, 22]
duplicate = []
for number in numbers:
    if number not in duplicate:
        duplicate.append(number)
print(duplicate)
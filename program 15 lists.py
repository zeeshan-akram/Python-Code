number = [34, 2, 44, 10, 3]
i = 0
largest = 0
for item in number:
    if item > number[i] and item > largest:
        largest = item

print(largest)
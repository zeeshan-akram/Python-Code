matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print(matrix[0][1])
print(matrix[1][0])
for item in matrix:
    for row in item:
        print(row, end='')
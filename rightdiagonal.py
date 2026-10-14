matrix = [
    [7, 2, 5],
    [9, 0, 3],
    [4, 9, 11]
]

right_diagonal_sum = 0
n = len(matrix)

for i in range(n):
    right_diagonal_sum += matrix[i][n - 1 - i]

print("Sum of Right Diagonal:", right_diagonal_sum)
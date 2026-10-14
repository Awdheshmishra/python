matrix = [
    [7, 2, 5],
    [9, 0, 3],
    [4, 9, 11]
]

left_diagonal_sum = 0

for i in range(len(matrix)):
    left_diagonal_sum += matrix[i][i]

print("Sum of Left Diagonal:", left_diagonal_sum)  

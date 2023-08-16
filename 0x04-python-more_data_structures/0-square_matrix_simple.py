#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result_matrix = [[0 for _ in row] for row in matrix]

    # Iterate through each element in the matrix and compute the square
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

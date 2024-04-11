def rotateImage(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in matrix:
        i.reverse()
    return matrix


print(rotateImage([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

[1, 4, 7]
[2, 5, 8]
[3, 6, 9]

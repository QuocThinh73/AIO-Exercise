import numpy as np


def compute_vector_length(vector):
    total = 0
    for v in vector:
        total += v**2
    len_of_vector = np.sqrt(total)
    return len_of_vector


def compute_dot_product(vector1, vector2):
    result = 0
    for v, u in zip(vector1, vector2):
        result += u * v
    return result


def matrix_multi_vector(matrix, vector):
    result = np.array([])
    for i in range(len(matrix)):
        tmp = 0
        for a, v in zip(matrix[i], vector):
            tmp += a * v
        result = np.append(result, tmp)
    return result


def matrix_multi_matrix(matrix1, matrix2):
    result = np.zeros((len(matrix1), len(matrix2)))
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            tmp = 0
            for index in range(len(matrix1[0])):
                tmp += matrix1[i][index] * matrix2[index][j]
            result[i][j] = tmp
    return result


def inverse_matrix(matrix):
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if determinant == 0:
        return None
    result = np.array([[matrix[1][1], -matrix[0][1]],
                       [-matrix[1][0], matrix[0][0]]], dtype=float)
    result *= (1 / determinant)
    return result


A = np.array([[-2, 6],
             [8, -4]])
print(inverse_matrix(A))

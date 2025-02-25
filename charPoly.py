import numpy.polynomial.polynomial as polynomial

"""def determinant(matrix, size):
    det=polynomial.Polynomial([0])
    if size ==0:
        return 1
    else:
        for i in range(size):
            det = det + (-1)**(i+1)*(polynomial.Polynomial([-1*matrix[i][size-1], 1]) if i != size else 0)*determinant(matrix, size-1)
            print(det)
        return det
print(determinant(A, 3))"""


# in the beginning only god and I knew how this worked
# currently only god (and chatGPT[is there a difference?]) knows"

def get_minor(matrix, row, col):
    return [matrix[i][:col] + matrix[i][col + 1:] for i in range(len(matrix)) if i != row]


def determinant(matrix):
    size = len(matrix)

    if size == 1:
        return matrix[0][0]

    det = polynomial.Polynomial([0])

    for col in range(size):
        minor = get_minor(matrix, 0, col)
        cofactor = (-1) ** col * matrix[0][col] * determinant(minor)
        det += cofactor

    return det


def characteristic_polynomial(matrix):
    size = len(matrix)
    lambda_poly = polynomial.Polynomial([0, 1])

    matrix_lambda = [
        [int(matrix[i][j]) - (lambda_poly if i == j else 0) for j in range(size)]
        for i in range(size)
    ]

    return determinant(matrix_lambda)


A = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 2]
]

char_poly = characteristic_polynomial(A)
print(char_poly)  # Should print λ^3 - 3λ^2 + 3λ - 1

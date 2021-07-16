from matrix_structure import Matrix
import random

def main():
    matrix_A = Matrix(3, 2)
    matrix_B = Matrix(2, 4)
    for r in range(matrix_A.numRows()):
        for c in range(matrix_A.numCols()):
            matrix_A[r, c] = random.randint(1, 10)

    for r in range(matrix_B.numRows()):
        for c in range(matrix_B.numCols()):
            matrix_B[r, c] = random.randint(1, 10)

    print("Matrix_A")
    for r in range(matrix_A.numRows()):
        for c in range(matrix_A.numCols()):
            print(matrix_A[r, c], end=' ')
        print()
    print()
    print("Matrix_B")
    for r in range(matrix_B.numRows()):
        for c in range(matrix_B.numCols()):
            print(matrix_B[r, c], end=' ')
        print()
    print()

    newMatrix = matrix_A * matrix_B

    print("newMatrix")
    for r in range(newMatrix.numRows()):
        for c in range(newMatrix.numCols()):
            print(newMatrix[r, c], end=' ')
        print()

main()

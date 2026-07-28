# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#


# Function to display a matrix neatly
def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end="\t")
        print()


# Function to read a matrix from the user
def read_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))

        # Ensure correct number of columns
        while len(row) != cols:
            print("Error: Enter exactly", cols, "values.")
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))

        matrix.append(row)

    return matrix



# PART A — Transpose Matrix


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for j in range(cols):
        new_row = []

        for i in range(rows):
            new_row.append(matrix[i][j])

        transpose.append(new_row)

    return transpose



# PART B — Add Two Matrices


def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []

    for i in range(rows):
        row = []

        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])

        result.append(row)

    return result

# PART C — Multiply Two Matrices

def multiply_matrices(matrix1, matrix2):
    rows_A = len(matrix1)
    cols_A = len(matrix1[0])

    rows_B = len(matrix2)
    cols_B = len(matrix2[0])

    result = []

    for i in range(rows_A):
        row = []

        for j in range(cols_B):
            total = 0

            for k in range(cols_A):
                total += matrix1[i][k] * matrix2[k][j]

            row.append(total)

        result.append(row)

    return result


# MAIN PROGRAM

print("PART A: Matrix Transpose")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = read_matrix(rows, cols)

print("\nOriginal Matrix:")
display_matrix(matrix)

transposed = transpose_matrix(matrix)

print("\nTransposed Matrix:")
display_matrix(transposed)


# PART B: Matrix Addition

print("\nPART B: Matrix Addition")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter Matrix A:")
matrix_A = read_matrix(rows, cols)

print("\nEnter Matrix B:")
matrix_B = read_matrix(rows, cols)

sum_matrix = add_matrices(matrix_A, matrix_B)

print("\nMatrix Addition Result:")
display_matrix(sum_matrix)


# PART C: Matrix Multiplication

print("\nPART C: Matrix Multiplication")

rows_A = int(input("Enter number of rows for Matrix A: "))
cols_A = int(input("Enter number of columns for Matrix A: "))

print("\nEnter Matrix A:")
matrix_A = read_matrix(rows_A, cols_A)


rows_B = int(input("Enter number of rows for Matrix B: "))
cols_B = int(input("Enter number of columns for Matrix B: "))


# Check multiplication condition
if cols_A != rows_B:
    print("Error: Matrix multiplication is not possible.")
else:
    print("\nEnter Matrix B:")
    matrix_B = read_matrix(rows_B, cols_B)

    product_matrix = multiply_matrices(matrix_A, matrix_B)

    print("\nMatrix Multiplication Result:")
    display_matrix(product_matrix)
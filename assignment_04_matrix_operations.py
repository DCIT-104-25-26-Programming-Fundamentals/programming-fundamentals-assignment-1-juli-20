# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols, name):
    """Read a matrix from the user"""
    print(f"\nEnter matrix {name}:")
    matrix = []
    for i in range(rows):
        row = []
        while True:
            try:
                values = input(f"Enter row {i + 1}: ").split()
                if len(values) != cols:
                    print(f"Error: Please enter exactly {cols} numbers.")
                    continue
                for val in values:
                    row.append(int(val))  # Changed to int
                break
            except ValueError:
                print("Error: Please enter valid numbers.")
                continue
        matrix.append(row)
    return matrix

def display_matrix(matrix, title="Matrix"):
    """Display a matrix in a neat grid format"""
    print(f"\n{title}:")
    for row in matrix:
        for num in row:
            print(f"{num:>8}", end="")
        print()

# =============================================================================
# PART A — Transpose a Matrix
# =============================================================================
def transpose_matrix():
    print("\n=== PART A: Transpose Matrix ===")
    
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    matrix = read_matrix(rows, cols, "A")
    display_matrix(matrix, "Original Matrix")
    
    # Transpose: rows become columns, columns become rows
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    
    display_matrix(transposed, "Transposed Matrix")

# =============================================================================
# PART B — Add Two Matrices
# =============================================================================
def add_matrices():
    print("\n=== PART B: Add Two Matrices ===")
    
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    matrix_a = read_matrix(rows, cols, "A")
    matrix_b = read_matrix(rows, cols, "B")
    
    display_matrix(matrix_a, "Matrix A")
    display_matrix(matrix_b, "Matrix B")
    
    # Add matrices element-wise
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)
    
    display_matrix(result, "Sum (A + B)")

# =============================================================================
# PART C — Multiply Two Matrices
# =============================================================================
def multiply_matrices():
    print("\n=== PART C: Multiply Two Matrices ===")
    
    # Read matrix A
    rows_a = int(input("Enter number of rows for matrix A: "))
    cols_a = int(input("Enter number of columns for matrix A: "))
    matrix_a = read_matrix(rows_a, cols_a, "A")
    
    # Read matrix B
    rows_b = int(input("\nEnter number of rows for matrix B: "))
    cols_b = int(input("Enter number of columns for matrix B: "))
    
    # Check if multiplication is possible
    if cols_a != rows_b:
        print(f"Error: Number of columns in A ({cols_a}) must equal number of rows in B ({rows_b})")
        return
    
    matrix_b = read_matrix(rows_b, cols_b, "B")
    
    display_matrix(matrix_a, "Matrix A")
    display_matrix(matrix_b, "Matrix B")
    
    # Multiply matrices: result[i][j] = sum of A[i][k] * B[k][j]
    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(total)
        result.append(new_row)
    
    display_matrix(result, "Product (A × B)")

# =============================================================================
# MAIN MENU
# =============================================================================
def main():
    while True:
        print("\n" + "=" * 40)
        print("       MATRIX OPERATIONS MENU")
        print("=" * 40)
        print("1. Transpose a Matrix")
        print("2. Add Two Matrices")
        print("3. Multiply Two Matrices")
        print("4. Quit")
        print("=" * 40)
        
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
        
        if choice == 1:
            transpose_matrix()
        elif choice == 2:
            add_matrices()
        elif choice == 3:
            multiply_matrices()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-4.")

# Call the main function
if __name__ == "__main__":
    main()
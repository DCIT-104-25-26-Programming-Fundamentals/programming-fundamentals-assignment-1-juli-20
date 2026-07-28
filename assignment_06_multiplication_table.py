# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_single_table(num):
    """Part A: Print multiplication table for a single number (1-12)"""
    print(f"\nMultiplication Table for {num}:")
    for i in range(1, 13):
        print(f"{num}  x  {i:2}  =  {num * i:3}")

def print_multiple_tables(n):
    """Part B: Print multiplication tables from 1 to N"""
    if n <= 0:
        print("Error: N must be a positive integer.")
        return
    
    for num in range(1, n + 1):
        print(f"\nMultiplication Table for {num}:")
        for i in range(1, 13):
            print(f"{num}  x  {i:2}  =  {num * i:3}")
        if num < n:
            print("-" * 27)

def main():
    while True:
        print("\n" + "=" * 40)
        print("    MULTIPLICATION TABLE GENERATOR")
        print("=" * 40)
        print("1. Print Single Table (1-12)")
        print("2. Print Tables from 1 to N")
        print("3. Quit")
        print("=" * 40)
        
        try:
            choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
        
        if choice == 1:
            try:
                num = int(input("Enter a number: "))
                print_single_table(num)
            except ValueError:
                print("Error: Please enter a valid number.")
        
        elif choice == 2:
            try:
                n = int(input("Enter a number (N): "))
                print_multiple_tables(n)
            except ValueError:
                print("Error: Please enter a valid number.")
        
        elif choice == 3:
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter 1-3.")

# Call the main function
if __name__ == "__main__":
    main() 
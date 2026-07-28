# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_sum(numbers):
    """Calculate the sum of all numbers in the list (without using sum())"""
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_average(numbers):
    """Calculate the average of all numbers in the list"""
    total = calculate_sum(numbers)
    return total / len(numbers)

def find_maximum(numbers):
    """Find the maximum number in the list (without using max())"""
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def find_minimum(numbers):
    """Find the minimum number in the list (without using min())"""
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def main():
    try:
        # Ask user how many numbers
        n = int(input("How many numbers? "))
        
        # Validate input
        if n <= 0:
            print("Error: N must be a positive integer.")
            return
        
        # Collect numbers from user
        numbers = []
        for i in range(n):
            num = float(input(f"Enter number {i + 1}: "))
            numbers.append(num)
        
        # Calculate statistics
        total = calculate_sum(numbers)
        average = calculate_average(numbers)
        maximum = find_maximum(numbers)
        minimum = find_minimum(numbers)
        
        # Display results
        print("\nResults:")
        print(f"Sum:     {total}")
        print(f"Average: {average}")
        print(f"Maximum: {maximum}")
        print(f"Minimum: {minimum}")
    
    except ValueError:
        print("Error: Please enter valid numbers.")

# Call the main function
if __name__ == "__main__":
    main()
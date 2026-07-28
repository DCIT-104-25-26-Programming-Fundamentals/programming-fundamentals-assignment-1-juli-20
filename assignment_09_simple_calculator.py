# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def display_menu():
    """Display the calculator menu"""
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")
    print("============================")

def add(a, b):
    """Return the sum of two numbers"""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers"""
    return a - b

def multiply(a, b):
    """Return the product of two numbers"""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers"""
    if b == 0:
        return None  # Return None for division by zero
    return a / b

def modulus(a, b):
    """Return the remainder of two numbers"""
    if b == 0:
        return None  # Return None for division by zero
    return a % b

def power(a, b):
    """Return a raised to the power of b"""
    return a ** b

def get_numbers():
    """Get two numbers from the user"""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers.")
        return None, None

def main():
    """Main program loop"""
    while True:
        display_menu()
        
        try:
            choice = int(input("Select an operation (1-7): "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
        
        # Quit
        if choice == 7:
            print("Goodbye!")
            break
        
        # Check for valid operation (1-6)
        if choice < 1 or choice > 6:
            print("Invalid choice! Please enter 1-7.")
            continue
        
        # Get numbers from user
        num1, num2 = get_numbers()
        if num1 is None or num2 is None:
            continue
        
        # Perform the selected operation
        if choice == 1:
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result:.2f}")
        
        elif choice == 2:
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result:.2f}")
        
        elif choice == 3:
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result:.2f}")
        
        elif choice == 4:
            result = divide(num1, num2)
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {num1} / {num2} = {result:.2f}")
        
        elif choice == 5:
            # Modulus only works with integers
            num1_int = int(num1)
            num2_int = int(num2)
            result = modulus(num1_int, num2_int)
            if result is None:
                print("Error: Cannot divide by zero for modulus.")
            else:
                print(f"Result: {num1_int} % {num2_int} = {result}")
        
        elif choice == 6:
            result = power(num1, num2)
            print(f"Result: {num1} ** {num2} = {result:.2f}")

# Call the main function
if __name__ == "__main__":
    main()

 # =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def display_menu():
    """Display the main menu"""
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")
    print("================================")

def add_student(students):
    """Feature 1: Add a new student"""
    print("\n--- Add Student ---")
    
    name = input("Student name: ")
    
    try:
        student_id = int(input("Student ID: "))
    except ValueError:
        print("Error: ID must be a number.")
        return
    
    try:
        num_scores = int(input("How many scores? "))
        if num_scores < 0:
            print("Error: Number of scores cannot be negative.")
            return
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    
    scores = []
    for i in range(num_scores):
        try:
            score = float(input(f"Enter score {i + 1}: "))
            scores.append(score)
        except ValueError:
            print("Error: Score must be a number.")
            return
    
    # Create student dictionary
    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    
    students.append(student)
    print(f'Student "{name}" added successfully.')

def display_all_students(students):
    """Feature 2: Display all students in a formatted table"""
    if not students:
        print("No students have been added yet.")
        return
    
    print("\n" + "-" * 60)
    print(f"{'Name':<15} {'ID':<12} {'Scores':<20} {'Average':<10}")
    print("-" * 60)
    
    for student in students:
        name = student["name"]
        student_id = student["id"]
        scores = student["scores"]
        
        # Format scores as a string
        scores_str = ", ".join(str(int(s)) for s in scores)
        
        # Calculate average
        if scores:
            avg = sum(scores) / len(scores)
            avg_str = f"{avg:.2f}"
        else:
            avg_str = "N/A"
        
        print(f"{name:<15} {student_id:<12} {scores_str:<20} {avg_str:<10}")
    
    print("-" * 60)

def calculate_average(students):
    """Feature 3: Calculate average score for a specific student"""
    if not students:
        print("No students in the system yet.")
        return
    
    try:
        search_id = int(input("Enter student ID: "))
    except ValueError:
        print("Error: ID must be a number.")
        return
    
    # Search for student by ID
    for student in students:
        if student["id"] == search_id:
            scores = student["scores"]
            if not scores:
                print(f"{student['name']} has no scores recorded.")
                return
            
            avg = sum(scores) / len(scores)
            print(f"{student['name']}'s average score: {avg:.2f}")
            return
    
    print(f"Error: Student with ID {search_id} not found.")

def main():
    """Main program loop"""
    students = []  # List to store all student records
    
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
        
        if choice == 1:
            add_student(students)
        elif choice == 2:
            display_all_students(students)
        elif choice == 3:
            calculate_average(students)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-4.")

# Call the main function
if __name__ == "__main__":
    main()
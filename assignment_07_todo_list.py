def display_menu():
    """Display the main menu"""
    print("\n============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")
    print("============================")

def add_task(tasks):
    """Feature 1: Add a task to the list"""
    task = input("Enter task: ")
    tasks.append(task)
    print(f'Task added: "{task}"')

def view_tasks(tasks):
    """Feature 2: View all tasks"""
    if not tasks:
        print("Your to-do list is empty. Add some tasks!")
        return
    
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task(tasks):
    """Feature 3: Delete a task from the list"""
    if not tasks:
        print("No tasks to delete! Your list is empty.")
        return
    
    # Show current tasks
    view_tasks(tasks)
    
    try:
        task_num = int(input("\nEnter task number to delete: "))
        
        # Check if task number is valid
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'Task "{removed_task}" has been removed.')
        else:
            print("Error: Invalid task number!")
    except ValueError:
        print("Error: Please enter a valid number.")

def main():
    """Main program loop"""
    tasks = []  # Empty list to store tasks
    
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
        
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            delete_task(tasks)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-4.")

# Call the main function
if __name__ == "__main__":
    main()
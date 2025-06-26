import os

# Function to display the menu
def display_menu():
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

# Function to view the to-do list
def view_todo_list(todo_list):
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            status = "Completed" if task['completed'] else "Not Completed"
            print(f"{index}. {task['description']} - {status}")

# Function to add a task to the to-do list
def add_task(todo_list):
    task_description = input("Enter the task description: ")
    todo_list.append({"description": task_description, "completed": False})
    print("Task added successfully.")

# Function to update a task in the to-do list
def update_task(todo_list):
    view_todo_list(todo_list)
    if todo_list:
        try:
            task_number = int(input("Enter the task number to update: "))
            if 1 <= task_number <= len(todo_list):
                new_description = input("Enter the new description: ")
                todo_list[task_number - 1]['description'] = new_description
                print("Task updated successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Function to delete a task from the to-do list
def delete_task(todo_list):
    view_todo_list(todo_list)
    if todo_list:
        try:
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(todo_list):
                todo_list.pop(task_number - 1)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Function to mark a task as completed
def mark_task_completed(todo_list):
    view_todo_list(todo_list)
    if todo_list:
        try:
            task_number = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_number <= len(todo_list):
                todo_list[task_number - 1]['completed'] = True
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            update_task(todo_list)
        elif choice == '4':
            delete_task(todo_list)
        elif choice == '5':
            mark_task_completed(todo_list)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

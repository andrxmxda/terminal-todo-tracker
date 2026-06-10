import os

TODO_FILE = "tasks.txt"

def load_tasks():
    """Loads tasks from the text file."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_all_tasks(tasks):
    """Overwrites the text file with the updated list of tasks."""
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def show_tasks(tasks):
    """Prints the current checklist to the terminal."""
    print("\n--- My Checklist ---")
    if not tasks:
        print("No tasks yet! Your schedule is clear. 😎")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")
    print("---------------------\n")

def add_task(task):
    """Appends a new task to the text file."""
    # New tasks start as incomplete: [ ]
    with open(TODO_FILE, "a") as file:
        file.write(f"[ ] {task}\n")

def main():
    """Main loop to handle user interaction."""
    while True:
        tasks = load_tasks()
        show_tasks(tasks)
        
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            new_task = input("Enter your task: ")
            if new_task.strip():
                add_task(new_task)
                print(f"Added: '{new_task}'")
                
        elif choice == "2":
            if not tasks:
                print("No tasks to complete!")
                continue
            try:
                task_num = int(input("Enter the task number to complete: "))
                if 1 <= task_num <= len(tasks):
                    # Change [ ] to [X] for the selected task
                    if tasks[task_num - 1].startswith("[ ]"):
                        tasks[task_num - 1] = tasks[task_num - 1].replace("[ ]", "[X]", 1)
                        save_all_tasks(tasks)
                        print("Task marked as completed! 🎉")
                    else:
                        print("That task is already completed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == "3":
            if not tasks:
                print("No tasks to delete!")
                continue
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    save_all_tasks(tasks)
                    print(f"Deleted: '{removed}'")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == "4":
            print("Goodbye! Stay productive.")
            break
        else:
            print("Invalid choice. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
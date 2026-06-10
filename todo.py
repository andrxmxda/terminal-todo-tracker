import os

# The text file where your tasks will be saved
TODO_FILE = "tasks.txt"

def load_tasks():
    """Loads tasks from the text file. Returns an empty list if the file doesn't exist."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def show_tasks(tasks):
    """Prints the current checklist to the terminal."""
    print("\n--- My Checklist ---")
    if not tasks:
        print("No tasks yet! Your schedule is clear. 😎")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. [ ] {task}")
    print("---------------------\n")

def add_task(task):
    """Appends a new task to the text file."""
    with open(TODO_FILE, "a") as file:
        file.write(f"{task}\n")

def main():
    """Main loop to handle user interaction in the terminal."""
    while True:
        tasks = load_tasks()
        show_tasks(tasks)
        
        print("1. Add Task")
        print("2. Exit")
        choice = input("Choose an option (1-2): ")
        
        if choice == "1":
            new_task = input("Enter your task: ")
            if new_task.strip():  # Don't add empty tasks
                add_task(new_task)
                print(f"Added: '{new_task}'")
        elif choice == "2":
            print("Goodbye! Stay productive.")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    main()

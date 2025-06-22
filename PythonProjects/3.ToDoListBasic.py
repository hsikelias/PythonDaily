import os
# from colorama import Fore, Style, init
# init(autoreset=True)

tasks = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def add_task():
    print("\n--- Add a Task ---")
    task_name = input("Task Name: ").strip()
    deadline = input("Deadline (MM/DD/YYYY): ").strip()
    time = input("Time (e.g. 14:30): ").strip()

    try:
        priority = int(input("Priority (1-5): "))
        if not (1 <= priority <= 5):
            raise ValueError
    except ValueError:
        print("Invalid priority. Please enter a number from 1 to 5.")
        return

    task = {
        "name": task_name,
        "deadline": deadline,
        "time": time,
        "priority": priority
    }

    tasks.insert(0, task)
    print("Task added successfully!")

def remove_task():
    if not tasks:
        print("No tasks to remove.")
        return

    print("\n--- Remove a Task ---")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task['name']} (Due: {task['deadline']} at {task['time']}, Priority: {task['priority']})")

    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed task: {removed['name']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def view_tasks():
    if not tasks:
        print("\nNo tasks added yet.")
    else:
        print("\n--- Your Tasks ---")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task['name']} (Due: {task['deadline']} at {task['time']}, Priority: {task['priority']})")

def main():
    while True:
        clear_screen()
        print("=-=-=-=-=-=-=-= TO-DO LIST =-=-=-=-=-=-=-=")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input bruh. Please enter a number between 1 and 4.")
            input("Press Enter to continue...")
            continue

        if choice == 1:
            add_task()
        elif choice == 2:
            remove_task()
        elif choice == 3:
            view_tasks()
        elif choice == 4:
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Please choose a valid option (1-4).")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

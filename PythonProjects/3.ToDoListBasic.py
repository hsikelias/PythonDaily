tasks = []

print("---------- To Do List ----------")

while True:
    print("\nSelect an operation:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    if choice == 1:
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
            continue

        task = {
            "name": task_name,
            "deadline": deadline,
            "time": time,
            "priority": priority
        }

        tasks.insert(0, task) 
        print("Task added successfully!")

    elif choice == 2:
        if not tasks:
            print("No tasks to remove.")
            continue

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

    elif choice == 3:
        if not tasks:
            print("\nNo tasks added yet.")
        else:
            print("\n--- Your Tasks ---")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task['name']} (Due: {task['deadline']} at {task['time']}, Priority: {task['priority']})")

    elif choice == 4:
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Please choose a valid option (1-4).")

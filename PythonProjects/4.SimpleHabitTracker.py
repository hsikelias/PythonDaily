import json

def load_habits():
    try:
        with open("habits.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_habits(habits):
    with open("habits.json", "w") as file:
        json.dump(habits, file, indent=2)

habits = load_habits()

while True: 
    print("\n=-=-=-=-=-=-=-= Habit Tracker =-=-=-=-=-=-=-=")
    print("1. Add new habit")
    print("2. Delete habit")
    print("3. View habits")
    print("4. Mark habit as completed")
    print("5. Exit")

    try: 
        choice = int(input("Choose an option (1-5): "))
    except ValueError:
        print("Invalid input. Use numbers only.")
        continue 

    if choice == 1:
        name = input("Enter habit name: ")
        try:
            count = int(input("How many days have you done it?: "))
        except ValueError:
            print("Enter a valid number.")
            continue
        habits.append({"Habit name": name, "Days Count": count})
        save_habits(habits)
        print(f"'{name}' added.")

    elif choice == 2:
        if not habits:
            print("⚠️ No habits to delete.")
            continue
        print("\nHabits:")
        for i, h in enumerate(habits):
            print(f"{i + 1}. {h['Habit name']} ({h['Days Count']} days)")
        try:
            index = int(input("Enter number to delete: ")) - 1
            if 0 <= index < len(habits):
                removed = habits.pop(index)
                save_habits(habits)
                print(f"Deleted: {removed['Habit name']}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a valid number.")

    elif choice == 3:
        if not habits:
            print("No habits to show.")
        else:
            print("\nYour Habits:")
            for i, h in enumerate(habits, 1):
                print(f"{i}. {h['Habit name']} - {h['Days Count']} days")

    elif choice == 4:
        if not habits:
            print("No habits to mark.")
            continue
        print("\nMark Habit as Completed:")
        for i, h in enumerate(habits):
            print(f"{i + 1}. {h['Habit name']} ({h['Days Count']} days)")
        try:
            index = int(input("Choose habit number: ")) - 1
            if 0 <= index < len(habits):
                habits[index]["Days Count"] += 1
                save_habits(habits)
                print(f"Updated '{habits[index]['Habit name']}' to {habits[index]['Days Count']} days!")
            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a valid number.")

    elif choice == 5:
        print("Goodbye! Keep tracking your habits.")
        break
    
    else:
        print("Choose a number from 1 to 5.")


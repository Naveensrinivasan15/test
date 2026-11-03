
tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks available!")
    else:
        print("\n--- YOUR TASKS ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        try:
            number = int(input("Enter task number to delete: "))
            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "4":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice! Try again.")

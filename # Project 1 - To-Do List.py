# Project 1 - To-Do List
# Python Programming

tasks = []

print("================================")
print("        MY TO-DO LIST")
print("================================")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Add a task
    if choice == "1":
        task = input("Enter your task: ")

        if task.strip() == "":
            print("Task cannot be empty.")
        else:
            tasks.append(task)
            print("Task added successfully!")

    # View all tasks
    elif choice == "2":
        print("\n-------- Your Tasks --------")

        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    # Exit
    elif choice == "3":
        print("\nThank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")
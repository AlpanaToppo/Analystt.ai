tasks_list = []

def show_tasks():
    if not tasks_list:
        print("\nNo tasks available.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks_list, start=1):
            print(f"{i}. {task}")

def add_task(task):
    tasks_list.append(task)
    print(f"Task '{task}' added successfully.")

def delete_task(index):
    if not tasks_list:
        print("No tasks available.")
    elif 1 <= index <= len(tasks_list):
        deleted_task = tasks_list.pop(index - 1)
        print(f"Task '{deleted_task}' deleted successfully.")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\n1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '3':
            index = int(input("Enter the task index to delete: "))
            delete_task(index)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

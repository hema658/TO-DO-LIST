todo_list = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f'"{task}" has been added to your To-Do list.')

def view_tasks():
    if not todo_list:
        print("Your To-Do list is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter the task number to remove: "))
            removed_task = todo_list.pop(task_num - 1)
            print(f'"{removed_task}" has been removed from your To-Do list.')
        except (ValueError, IndexError):
            print("Invalid task number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting... Have a productive day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__== "__main__":
    main()
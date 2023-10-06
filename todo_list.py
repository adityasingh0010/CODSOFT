
tasks = []


def create_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task created successfully!")


def track_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        print("Your tasks:")
        for index, task in enumerate(tasks):
            print("{} {}".format(index + 1, task))



def mark_completed():
    if not tasks:
        print("No tasks found!")
    else:
        track_tasks()
        try:
            task_num = int(input("Enter the task number you want to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                print("Task '{}' marked as completed!".format(tasks[task_num - 1]))

                tasks.pop(task_num - 1)
            else:
                print("Invalid task number!")
        except ValueError:
            print("Invalid input! Please enter a valid task number.")

def update_task():
    if not tasks:
        print("No tasks found!")
    else:
        track_tasks()
        try:
            task_num = int(input("Enter the task number you want to update: "))
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter the updated task: ")
                tasks[task_num - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Invalid input! Please enter a valid task number.")

def main():
    print("Welcome to the To-Do List App!")

    while True:
        print("\nMenu:")
        print("1. Create Task")
        print("2. Track Tasks")
        print("3. Mark Task as Completed")
        print("4. Upadated Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            create_task()
        elif choice == '2':
            track_tasks()
        elif choice == '3':
            mark_completed()
        elif choice == '4' :
            update_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()

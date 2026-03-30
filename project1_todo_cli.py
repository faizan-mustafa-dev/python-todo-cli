tasks = []

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    ip = int(input("Enter Choice: "))

    if ip == 1:
        add_task = input("Please enter the task: ")
        tasks.append(add_task)
        print("Task added!")

    elif ip == 2:
        print("Your tasks: ")
        for i, task in enumerate(tasks):
            print(i, " - ", task)
    
    elif ip == 3:
        index = int(input("Please enter task index to delete: "))
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task deleted!")
        else:
            print("Invalid index")
    
    elif ip == 4:
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice!")

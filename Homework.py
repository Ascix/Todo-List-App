task_list = {}

def main_menu():
    command = input("""Main Menu
Press 1 to add task
Press 2 to delete task
Press 3 to view all tasks
Press q to quit
: """)
    if command == "q":
        print("Exiting To-Do List.")
        quit()
    elif command == "1":
        add_task()
        main_menu()
    elif command == "2":
        print(f"{task_list[i]} - {task_list[{task}]} - {task_list[{priority}]}")

        main_menu()
    elif command == "3":
        for i in task_list:
            print(f"{task_list[i]} - {task_list[{task}]} - {task_list[{priority}]}")
        delete = input("Which number do you want to delete?")
        del task_list[{delete}]
        main_menu()
    else:
        print("That option is not valid!")
        main_menu()


def add_task():
    task = input("What is your task? ") 
    priority = input("Priority (high, medium, or low): ").lower()        
    if priority == "high" or priority == "medium" or priority == "low":
        for i in task_list:
            task_list["{task}"] = "{priority}"
        print(f"Added task: {task.lower().capitalize()} - {priority.lower()} priority.")
    else:
        print("That option is not valid!")
        add_task()

main_menu()
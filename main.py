MIN_MENU = 1
MAX_MENU = 5

menus = {
    "Add Task" : 1,
    "View Task" : 2,
    "Mark Task as Complete" : 3,
    "Delete Task" : 4,
    "Exit" : 5
}




task = {1 : {"title" : "Read Chemistry", "status" : False}}


def menu():
    print("===TO-DO-LIST===")
    print()
    print("1) Add Task")
    print("2) View Tasks")
    print("3) Mark Task as Complete")
    print("4) Delete Task")
    print("5) Exit")


def user_choice():
    while True:
        choice = input("Enter Your Choice: ")
        if choice.isdigit():
            choice = int(choice)
            if MIN_MENU <= choice <= MAX_MENU:
                return choice
            else:
                print(f"⚠️Enter from the above menu {MIN_MENU} - {MAX_MENU}")
        else:
            print("⚠️Enter a valid number")

def add_task(tasks):
    user_input = input(f"Enter you new Task: ").title().strip()
    if len(user_input) > 0:
        tasks[max(tasks) + 1] = {"title" : user_input, "status" : False} 
    print(f"✅ Task {user_input} added")

    return user_input

def view_task(tasks):
    print("📋 Your Tasks")
    for i , j in tasks.items():
        if j["status"] == True:
            print(f"[{i}] ✅ {j["title"]}")
        else:
            print(f"[{i}] ❌ {j["title"]}")


def main():

    menu()
    choice = user_choice()
    if choice == 1:
        add_task(task)
    elif choice == 2:
        view_task(task)


main()
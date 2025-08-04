MIN_MENU = 1
MAX_MENU = 5

menus = {
    "Add Task" : 1,
    "View Task" : 2,
    "Mark Task as Complete" : 3,
    "Delete Task" : 4,
    "Exit" : 5
}



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
        choice = input("Enter Your Choice")
        if choice.isdigit():
            choice = int(choice)
            if MIN_MENU <= choice <= MAX_MENU:
                return choice
            else:
                print(f"⚠️Enter from the above menu {MIN_MENU} - {MAX_MENU}")
        else:
            print("⚠️Enter a valid number")

def add_task():
    user_input = input(f"Enter you new Task: ").capitalize()
    print(f"✅ Task {user_input} added")

    return user_input

def view_task():
    print("📋 Your Tasks")
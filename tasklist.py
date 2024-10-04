def add_task():
    task = input("Please enter a task to add to your task list: ")
    due_date = input("Enter a due date (optional) in the format DD/MM/YYYY or leave it blank: ")
    if due_date:
        task_entry = {"task": task, "due_date": due_date}
    else:
        task_entry = {"task": task}
    tasklist.append(task_entry)
    print(f"Task '{task}' has been added to the list.")


    def show_tasklist():
    if not tasklist:
        print("Your task list is empty.")
    else:
        print("Your tasks:")
        for task_entry in tasklist:
            task = task_entry["task"]
            due_date = task_entry.get("due_date", "No due date")
            print(f"- {task} (Due: {due_date})")



def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a task")
        print("2. Show task list")
        print("3. Exit the program")
        choice = input("Select an option (1/2/3): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasklist()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()            

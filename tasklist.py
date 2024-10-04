tasklist = []

def add_task():
    # Ask the user to input a task
    task = input("Please enter a task to add to your task list: ")
    
    # Ask the user for a due date (optional)
    due_date = input("Enter a due date (optional) in the format DD/MM/YYYY or leave it blank: ")
    
    # Ask for priority
    priority = input("Enter the priority (high, medium, low): ").lower()
    
    # Create a task entry with or without a due date
    if due_date:
        task_entry = {"task": task, "due_date": due_date, "priority": priority}
    else:
        task_entry = {"task": task, "priority": priority}
    
    # Add the task to the task list
    tasklist.append(task_entry)
    
    # Print the task details to debug
    print(f"Task: {task}, Due Date: {due_date}, Priority: {priority}")

    # Notify the user that the task has been added
    print(f"Task '{task}' with priority '{priority}' has been added to the list.")


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




def add_task():
    task = input("Please enter a task: ")
    due_date = input("Enter a due date (optional): ")
    priority = input("Enter the priority (high, medium, low): ").lower()
    task_entry = {"task": task, "due_date": due_date, "priority": priority}
    tasklist.append(task_entry)
    print(f"Task '{task}' with priority '{priority}' has been added.") 

import csv

def export_to_csv():
    with open("tasklist.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["task", "due_date", "priority"])
        writer.writeheader()
        for task in tasklist:
            writer.writerow(task)
    print("Task list has been exported to CSV.")


print(f"Task: {task}, Due Date: {due_date}, Priority: {priority}")


def add_task():
    task = input("Please enter a task to add to your task list: ")
    due_date = input("Enter a due date (optional) in the format DD/MM/YYYY or leave it blank: ")
    if due_date:
        task_entry = {"task": task, "due_date": due_date}
    else:
        task_entry = {"task": task}
    tasklist.append(task_entry)
    print(f"Task '{task}' has been added to the list.")

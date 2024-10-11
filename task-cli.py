#!/usr/bin/env python3

import json

def load_tasks(file_name="tasks.json"):
    try:
        with open(file_name, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks, file_name="tasks.json"):
    with open(file_name, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    description = input("Enter task description: ")
    task = {"id": len(tasks) + 1, "description": description, "status": "In Progress"}
    tasks.append(task)

def view_tasks(tasks):
    for task in tasks:
        print(f'{task["id"]}: {task["description"]} [{task["status"]}]')

# def update_task(tasks):
# def delete_task(tasks):

def main():
    tasks = load_tasks()

    while True:
        print("\nTask Tracker")
        print("[add] Add a task")
        print("[view] View all tasks")
        print("[quit] Save")

        choice = input("Enter choice: ")

        if choice.lower() == "add":
            add_task(tasks)
        elif choice.lower() == "view":
            view_tasks(tasks)
        elif choice.lower() == "quit":
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
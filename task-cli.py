#!/usr/bin/env python3

import json
import datetime
import sys

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

def add_task(tasks, description):
    timestamp = datetime.datetime.now().isoformat()
    task = {
        "id": len(tasks) + 1, 
        "description": description, 
        "status": "In Progress",
        "createdAt": timestamp,
        "updatedAt": timestamp}
    tasks.append(task)

def update_task(tasks, task_id, description):
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = datetime.datetime.now().isoformat()

def update_status(tasks, task_id, status):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
        
def delete_task(tasks, task_id):
    tasks[:] = [task for task in tasks if task["id"] != task_id]

def list_tasks(tasks, status=None):
    if not tasks:
        print("There are currently no tasks. Please add a task.")

    if status == "in-progress":
        for task in tasks:
            if task["status"] == "In Progress":
                print(f'{task["id"]}: {task["description"]} [{task["status"]}]')
    elif status == "done":
        for task in tasks:
            if task["status"] == "Done":
                print(f'{task["id"]}: {task["description"]} [{task["status"]}]')
    else:
        for task in tasks:
            print(f'{task["id"]}: {task["description"]} [{task["status"]}]')

def main():
    tasks = load_tasks()

    args = sys.argv

    try:
        if args[1].lower() == "add":
            description = args[2]
            add_task(tasks, description)
        elif args[1].lower() == "update":
            task_id, new_description = int(args[2]), args[3]
            update_task(tasks, task_id, new_description)
        elif args[1].lower() == "status":
            task_id, new_status = int(args[2]), args[3]
            update_status(tasks, task_id, new_status)
        elif args[1].lower() == "delete":
            task_id = int(args[2])
            delete_task(tasks, task_id)
        elif args[1].lower() == "list":
            try:
                status = args[2]
                list_tasks(tasks, status)
            except IndexError:
                list_tasks(tasks)
        else:
            print("Please try again.")
    except IndexError:
        print("Needs more details.")

    save_tasks(tasks)

if __name__ == "__main__":
    main()
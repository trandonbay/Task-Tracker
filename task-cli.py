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
        "status": "todo",
        "createdAt": timestamp,
        "updatedAt": timestamp}
    tasks.append(task)
    print(f"Task added successfully. (ID: {task['id']})")

def update_task(tasks, task_id, description=None, status=None):
    for task in tasks:
        if task["id"] == task_id:
            if description:
                task["description"] = description
            if status:
                task["status"] = status
        task["updatedAt"] = datetime.datetime.now().isoformat()
        
def delete_task(tasks, task_id):
    tasks[:] = [task for task in tasks if task["id"] != task_id]

def list_tasks(tasks, status=None):
    filtered_tasks = [task for task in tasks if not status or task["status"] == status]

    if not filtered_tasks:
        print("There are currently no tasks. Please add a task.")

    for task in filtered_tasks:
        print(f'{task["id"]}: {task["description"]} [{task["status"]}]')

def main():
    args = sys.argv[1:]

    tasks = load_tasks()

    command_map = {
        "add": add_task,
        "new": add_task, # alias for add
        "update": update_task,
        "modify": update_task, # alias for update
        "mark-in-progress": lambda tasks, task_id: update_task(tasks, task_id, status="in-progress"),
        "in-progress": lambda tasks, task_id: update_task(tasks, task_id, status="in-progress"),
        "mark-done": lambda tasks, task_id: update_task(tasks, task_id, status="done"),
        "done": lambda tasks, task_id: update_task(tasks, task_id, status="done"),
        "delete": delete_task,
        "remove": delete_task,
        "list": list_tasks,
        "view": list_tasks,
    }

    if not args:
        print("Please provide a command.")
        return

    command = args[0].lower()

    if command in command_map:
        try:
            if command in ["add", "new"]:
                description = args[1]
                command_map[command](tasks, description)
            elif command in ["update", "modify"]:
                task_id = int(args[1])
                description = args[2]
                command_map[command](tasks, task_id, description=description)
            elif command in ["mark-in-progress", "in-progress", "mark-done", "done"]:
                task_id = int(args[1])
                command_map[command](tasks, task_id)
            elif command in ["delete", "remove"]:
                task_id = int(args[1])
                command_map[command](tasks, task_id)
            elif command in ["list", "view"]:
                try:
                    status = args[1]
                    command_map[command](tasks, status)
                except IndexError:
                    command_map[command](tasks)
        except IndexError:
            print(f"Command '{command}' requires additional arguments.")
    else:
        print(f"Unknown command: {command}")

    save_tasks(tasks)

if __name__ == "__main__":
    main()
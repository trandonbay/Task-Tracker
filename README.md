# Task CLI

A simple command-line interface (CLI) task manager written in Python. This application allows you to manage your tasks through a series of commands, including adding, updating, deleting, and listing tasks.

## Features

- Add tasks with descriptions
- Update task descriptions and statuses
- Delete tasks
- List all tasks or filter by status
- Store tasks in a JSON file

## Commands
### Add a Task
```
task-cli.py.py add "Task description"
```

### Update a Task
#### To update a task's description
```
task-cli.py.py update <task_id> "New task description"
```
#### To update a task's status
```
task-cli.py.py update mark-in-progress <task_id>
```
or
```
task-cli.py.py update done <task_id>
```

### Delete a Task
```
task-cli.py.py delete <task_id>
```
### List Tasks
#### To list all tasks
```
task-cli.py.py list
```
#### To list tasks filtered by status
```
task-cli.py.py list in-progress
```
or
```
task-cli.py.py list done
```

## Command Aliases
- Add: `add`, `new`
- Update: `update`, `modify`
- Mark In Progress: `mark-in-progress`, `in-progress`
- Mark Done: `mark-done`, `done`
- Delete: `delete`, `remove`
- List: `list`, `show`

## JSON Storage
Tasks are stored in a JSON file named tasks.json. If the file does not exist, it will be created automatically when you add the first task.

## Example
```bash
# Adding a new task
task-cli.py add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli.py update 1 "Buy groceries and cook dinner"
task-cli.py delete 1

# Marking a task as in progress or done
task-cli.py mark-in-progress 1
task-cli.py mark-done 1

# Listing all tasks
task-cli.py list

# Listing tasks by status
task-cli.py list done
task-cli.py list todo
task-cli.py list in-progress
```
"""
QUESTION:
Create a function to implement the core logic for a to-do list, allowing users to create, delete, and mark tasks as completed. The function should be able to store and retrieve tasks, including their status. 

No specific database or UI implementation details are required; focus on the core logic for managing tasks. The function should be able to handle the following operations:

- Create a new task with an optional description
- Delete a task by its identifier
- Mark a task as completed by its identifier

The function should return a dictionary containing the task's identifier, name, description, and completion status. 

Restrictions: The function should be implemented in Python.
"""

def todo_list_manager(tasks=None):
    if tasks is None:
        tasks = {}

    def create_task(task_id, name, description=""):
        tasks[task_id] = {"name": name, "description": description, "completed": False}
        return tasks[task_id]

    def delete_task(task_id):
        if task_id in tasks:
            del tasks[task_id]
        return tasks

    def mark_task_completed(task_id):
        if task_id in tasks:
            tasks[task_id]["completed"] = True
        return tasks[task_id]

    return create_task, delete_task, mark_task_completed

# usage
create_task, delete_task, mark_task_completed = todo_list_manager()
task_id = 1
print(create_task(task_id, "Task 1", "This is task 1"))
print(mark_task_completed(task_id))
print(delete_task(task_id))
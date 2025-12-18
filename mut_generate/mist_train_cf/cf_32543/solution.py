"""
QUESTION:
Implement the `update_todo` function with the following signature: `def update_todo(todo_id: int, payload: dict) -> Todo`. The function should update a todo item in a list of Todo objects based on the provided todo ID and a payload containing the updated title and description. After updating the todo item, return the updated Todo object. Assume that the list of Todo objects is already defined and accessible within the function. 

Note that the Todo object has `title` and `description` attributes. The `payload` is a dictionary containing the updated `title` and `description`.
"""

class Todo:
    def __init__(self, title, description):
        self.title = title
        self.description = description

def update_todo(todo_id: int, todos, payload: dict) -> Todo:
    todo = todos[todo_id]
    todo.title = payload['title']
    todo.description = payload['description']
    return todo
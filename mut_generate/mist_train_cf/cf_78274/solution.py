"""
QUESTION:
Implement a function `undo_redo_stacks` that allows for undo and redo operations using a stack data structure with a limit of 10 most recent operations. The function should include `execute_operation`, `undo`, and `redo` methods to execute an operation, undo the last operation, and redo the last undone operation, respectively. Use an optimal approach to limit the undo and redo history, and provide a solution with a time complexity of O(1) and space complexity of O(n).
"""

from collections import deque

def undo_redo_stacks(limit=10):
    undoStack = deque([], maxlen=limit)
    redoStack = deque([], maxlen=limit)

    def execute_operation(operation):
        undoStack.append(operation)
        redoStack.clear()

    def undo():
        if len(undoStack) > 0:
            last_operation = undoStack.pop()
            redoStack.append(last_operation)
            print("Undo operation: ", last_operation)

    def redo():
        if len(redoStack) > 0:
            last_undo_operation = redoStack.pop()
            undoStack.append(last_undo_operation)
            print("Redo operation: ", last_undo_operation)

    return execute_operation, undo, redo
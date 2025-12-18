"""
QUESTION:
Write a function named `task_notes_count` that takes in a list of tasks and a list of notes, where each note is associated with a task. The function should return a dictionary where the keys are task names and the values are the number of notes associated with each task.
"""

def task_notes_count(tasks, notes):
    task_notes = {}
    for task in tasks:
        task_notes[task] = 0
    for note in notes:
        task = note['task']
        if task in task_notes:
            task_notes[task] += 1
    return task_notes
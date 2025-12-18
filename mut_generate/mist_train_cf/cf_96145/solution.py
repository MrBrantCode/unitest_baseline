"""
QUESTION:
Write a function named `split_tasks` that takes a string of tasks as input. The string may contain tasks separated by commas, semicolons, or periods, and some tasks may have additional instructions enclosed in parentheses. Remove the instructions enclosed in parentheses and split the string into a list of tasks. The function should return the list of tasks with empty tasks removed.
"""

import re

def split_tasks(string):
    string = re.sub(r'\([^()]*\)', '', string)
    tasks = re.split(r'\s*,\s*|\s*;\s*|\s*\.\s*', string)
    tasks = [task.strip() for task in tasks if task.strip()]
    return tasks
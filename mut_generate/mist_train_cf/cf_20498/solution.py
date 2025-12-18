"""
QUESTION:
Write a function called `split_tasks` that takes a string as input and returns a list of tasks. The input string contains tasks separated by commas, semicolons, or periods, and some tasks may have additional instructions enclosed in parentheses. The function should remove these instructions and any empty tasks before returning the list.
"""

import re

def split_tasks(string):
    # Remove instructions enclosed in parentheses using regular expressions
    string = re.sub(r'\([^()]*\)', '', string)
    # Split the string into a list of tasks
    tasks = re.split(r'\s*,\s*|\s*;\s*|\s*\.\s*', string)
    # Remove any empty tasks from the list
    tasks = [task.strip() for task in tasks if task.strip()]
    return tasks
"""
QUESTION:
Create a function `categorize_todo(todo_list)` that takes a list of TODO items as input where each item is a string starting with "# TODO:" followed by a description of the task. The function should categorize each TODO item into one of the predefined categories ("Integration", "Functions", "Manifest", "Constants", "Locale", "Optimization", "CLI", "Update", "Documentation") and return a dictionary with the categories as keys and the number of tasks in each category as values. The categorization should be case-insensitive.
"""

from typing import List, Dict

def categorize_todo(todo_list: List[str]) -> Dict[str, int]:
    categories = {
        "Integration": 0,
        "Functions": 0,
        "Manifest": 0,
        "Constants": 0,
        "Locale": 0,
        "Optimization": 0,
        "CLI": 0,
        "Update": 0,
        "Documentation": 0
    }

    for todo in todo_list:
        category = todo.split(":")[1].strip().split()[0].capitalize()
        if category in categories:
            categories[category] += 1

    return categories
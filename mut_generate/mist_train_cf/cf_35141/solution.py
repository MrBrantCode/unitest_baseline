"""
QUESTION:
Write a function `format_careplan_item` that takes a care plan item category and a version key as input and returns a formatted string representing the item's category and version. The category can be either 'careplan_goal' or 'careplan_task', and the version is an integer. The function should use the category names provided by the dictionary CAREPLAN_CASE_NAMES = {'careplan_goal': 'Goal', 'careplan_task': 'Task'} to return a string in the format "{Category Name} - Version {version}". If the category is not found in the dictionary, it should return "Unknown Category" as the category name.
"""

def format_careplan_item(category, version):
    CAREPLAN_CASE_NAMES = {
        'careplan_goal': 'Goal',
        'careplan_task': 'Task'
    }
    category_name = CAREPLAN_CASE_NAMES.get(category, 'Unknown Category')
    return f"{category_name} - Version {version}"
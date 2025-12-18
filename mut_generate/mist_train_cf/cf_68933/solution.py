"""
QUESTION:
Develop a function named `calculate_average_grade` that takes a list of dictionaries as input. Each dictionary represents an entry with keys 'item_code', 'attribute_code', and 'grade'. The function should calculate the average grade for each item by performing a weighted average of ratings committed to distinctive attributes. Assuming equal weights for all attributes, return a dictionary where keys are item codes and values are their corresponding average grades.
"""

from collections import defaultdict

def calculate_average_grade(data):
    """
    Calculate the average grade for each item by performing a weighted average of ratings committed to distinctive attributes.

    Args:
    data (list): A list of dictionaries, where each dictionary contains 'item_code', 'attribute_code', and 'grade' keys.

    Returns:
    dict: A dictionary where keys are item codes and values are their corresponding average grades.
    """
    # defaultdict to hold sum of grades and counts for each item
    item_grades = defaultdict(lambda: {"sum": 0, "count": 0})

    # process data
    for entry in data:
        item = entry["item_code"]
        grade = entry["grade"]
        item_grades[item]["sum"] += grade
        item_grades[item]["count"] += 1

    # calculate average grades
    average_grades = {}
    for item, grades in item_grades.items():
        avg_grade = grades["sum"] / grades["count"]
        average_grades[item] = avg_grade

    return average_grades
"""
QUESTION:
Create a function named `sort_students` that takes a dictionary as input where keys are student names and values are their corresponding scores. The function should return a new dictionary with the students sorted in descending order based on their scores. The function should not modify the original dictionary.
"""

def sort_students(dictionary):
    sorted_students = {}
    sorted_names = sorted(dictionary, key=dictionary.get, reverse=True)
    for name in sorted_names:
        sorted_students[name] = dictionary[name]
    return sorted_students
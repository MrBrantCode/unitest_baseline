"""
QUESTION:
Create a function `highest_mark_students` that takes a dictionary `marks` where keys are student names and values are their marks. The function should return the name of the student with the highest mark as a string. If there are multiple students with the same highest mark, return a list of their names. The function should be able to handle dictionaries with any number of students.
"""

from typing import Union, List

def highest_mark_students(marks: dict) -> Union[str, List[str]]:
    max_mark = max(marks.values())
    top_students = [name for name, mark in marks.items() if mark == max_mark]
    if len(top_students) == 1:
        return top_students[0]
    else:
        return top_students
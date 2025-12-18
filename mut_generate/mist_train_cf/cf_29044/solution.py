"""
QUESTION:
Implement a function `highest_scoring_student` that takes a dictionary `scores` where keys are student names and values are their test scores. Return the name of the student with the highest score as a string if there is only one, otherwise return a list of their names in alphabetical order.
"""

from typing import Dict, List, Union

def highest_scoring_student(scores: Dict[str, int]) -> Union[str, List[str]]:
    max_score = max(scores.values())
    top_students = [name for name, score in scores.items() if score == max_score]
    if len(top_students) == 1:
        return top_students[0]
    else:
        return sorted(top_students)
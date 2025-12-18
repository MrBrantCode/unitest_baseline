"""
QUESTION:
Write a function `final_value_of_num(assignments)` that takes a list of strings representing sequential assignments to a variable `num` in the format "num = x", where x is an integer, and returns the final value of `num` after all the assignments have been executed. The function should not assume any initial value of `num`.
"""

from typing import List

def final_value_of_num(assignments: List[str]) -> int:
    num = None
    for assignment in assignments:
        num = int(assignment.split(' = ')[1])
    return num
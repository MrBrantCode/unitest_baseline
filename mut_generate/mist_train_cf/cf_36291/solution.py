"""
QUESTION:
Given a list of class schedules, where each schedule is a tuple of two integers representing the start and end time of the class, write a function `schedule(classes)` that takes this list and returns a subset of non-overlapping classes that can be attended, maximizing the number of classes attended. The input list `classes` is a list of tuples, where each tuple contains two integers representing the start and end time of a class. The function should return a list of tuples representing the maximum number of non-overlapping classes that can be attended.
"""

from typing import List, Tuple

def entance(classes: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if not classes:
        return []

    classes.sort(key=lambda x: x[1])  
    possible_classes = [classes[0]]  
    for i in range(1, len(classes)):
        if possible_classes[-1][1] <= classes[i][0]:  
            possible_classes.append(classes[i])  

    return possible_classes
"""
QUESTION:
You are given a list of strings, where each string represents answers to a set of questions. The strings are grouped by an empty line. Your task is to write a function `calculate_unique_answers(lines)` that calculates the sum of the counts of unique answers for each group. The function should take in a list of strings `lines` and return the total sum. The empty lines are used to separate different groups of people, and the count of unique answers for each group is the total number of distinct answers given by any person in the group.
"""

from typing import List

def calculate_unique_answers(lines: List[str]) -> int:
    total_unique_answers = 0
    group_answers = set()
    
    for line in lines:
        if line == "\n":
            total_unique_answers += len(group_answers)
            group_answers = set()
        else:
            for answer in line.strip("\n"):
                group_answers.add(answer)
    
    total_unique_answers += len(group_answers)  # Add the unique answers from the last group
    return total_unique_answers
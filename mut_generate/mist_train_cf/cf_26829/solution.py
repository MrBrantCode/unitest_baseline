"""
QUESTION:
Write a function `count_yes_answers(log: List[str]) -> Tuple[int, int]` that takes in a list of strings representing a log of responses from a group of people answering a series of yes-or-no questions. The function should return a tuple containing two integers: 
1. The total count of questions to which anyone in the group answered "yes".
2. The total count of questions to which everyone in the group answered "yes". 
Assume that each person's answers are recorded on a separate line, and the log is terminated by an empty line.
"""

from typing import List, Tuple

def count_yes_answers(log: List[str]) -> Tuple[int, int]:
    total_any_yes = 0
    total_all_yes = 0
    group_answers = {}
    person_count = 0

    for line in log:
        if not line.strip():  
            total_any_yes += len(group_answers)
            total_all_yes += sum(1 for count in group_answers.values() if count == person_count)
            group_answers = {}
            person_count = 0
        else:
            person_count += 1
            for char in line.strip():
                group_answers[char] = group_answers.get(char, 0) + 1

    # Account for the last group
    total_any_yes += len(group_answers)
    total_all_yes += sum(1 for count in group_answers.values() if count == person_count)

    return total_any_yes, total_all_yes
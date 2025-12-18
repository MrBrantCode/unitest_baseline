"""
QUESTION:
You are tasked with creating a function `count_every_yeses` that takes a list of groups, where each group is a list of strings representing the answers of a single person, and returns the sum of the count of questions to which everyone in the group answered "yes" for each group. The function should count the common characters (questions) in all strings (answers) within each group and sum up the counts from all groups.
"""

def count_every_yeses(groups):
    count = 0
    for group in groups:
        common_answers = set(group[0])
        for person_answers in group[1:]:
            common_answers = common_answers.intersection(set(person_answers))
        count += len(common_answers)
    return count
"""
QUESTION:
Write a function named `count_target_occurrences` that takes a list of integers and a target integer as parameters. The list will have between 10 and 100 elements, and the target integer will be within the range of -100 to 100. The function should return the number of times the target integer appears in the list.
"""

def count_target_occurrences(lst, target):
    count = 0
    for num in lst:
        if num == target:
            count += 1
    return count
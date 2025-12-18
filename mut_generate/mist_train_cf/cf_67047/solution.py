"""
QUESTION:
Write a function called `find_pair` that takes two inputs: a list of distinct positive integers `numbers` and a target integer `target`. The function should return a tuple of two integers from the list whose sum equals the target. If no such pair exists, the function should return `None`.
"""

def find_pair(numbers, target):
    # I'm going to use a set to keep track of the numbers we've seen
    seen = set()
    for number in numbers:
        # If the difference between the target and the current number is in the set, we've found our pair
        if target - number in seen:
            return (target - number, number)
        else:
            seen.add(number)
    return None
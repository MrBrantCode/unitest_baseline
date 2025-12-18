"""
QUESTION:
Write a function named `completed_goals_percentage` that calculates the percentage of completed goals from a given list of goals. The function should iterate through the list, treating each truthy value as a completed goal and each falsy value as an incomplete goal. The function should return the percentage of completed goals as a float, rounded to two decimal places is not required. The input list may contain any type of values, but the function should only consider the truthiness of each value.
"""

def completed_goals_percentage(goals):
    return (sum(1 for goal in goals if goal) / len(goals)) * 100
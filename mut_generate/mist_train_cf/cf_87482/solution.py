"""
QUESTION:
Create a function `group_numbers` that takes an array of numbers and a list of conditions as input. Each condition is a function that takes a number as input and returns a boolean. The function should group the numbers in the array based on the conditions and return a dictionary where the keys are the group names ('Group 1', 'Group 2', etc.) and the values are lists of numbers that satisfy the corresponding condition. Each number should be added to the first group for which it satisfies the condition.
"""

def group_numbers(array, conditions):
    groups = {}
    for num in array:
        for i, condition in enumerate(conditions):
            if condition(num):
                if f'Group {i+1}' in groups:
                    groups[f'Group {i+1}'].append(num)
                else:
                    groups[f'Group {i+1}'] = [num]
                break
    return groups
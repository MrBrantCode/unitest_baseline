"""
QUESTION:
Create a function named `group_by_rule` that takes a list of unique positive integers and a rule function as parameters. The rule function should be called on pairs of items from the list. If the rule function returns True, the two items will be placed in the same subgroup. The function should return a list of subgroups, where each subgroup contains numbers that satisfy the given rule. The rule is that the absolute difference between any two numbers in a subgroup should be less than or equal to a specified range.
"""

def group_by_rule(lst, rule):
    # Initialize the list of subgroups
    subgroups = []
    
    # For each item in the list
    for item in lst:
        # Try to find a subgroup that it fits into
        for subgroup in subgroups:
            if rule(subgroup[0], item):
                # If it fits, add it to the subgroup and break out of the inner loop
                subgroup.append(item)
                break
        else:
            # If no suitable subgroup was found, create a new one
            subgroups.append([item])
    return subgroups
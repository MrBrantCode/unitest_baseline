"""
QUESTION:
Write a function `calculate_alloy_needed` that determines the amount of each alloy needed to produce a certain amount of metal Y, given the concentration of metal Y in each alloy and the available amount of each alloy. The function should take in three parameters: `target_amount` (the amount of metal Y to be produced), `alloys` (a list of tuples, where each tuple contains the concentration and available amount of an alloy), and return a tuple of the amount of each alloy needed.
"""

def calculate_alloy_needed(target_amount, alloys):
    # Sort the alloys in descending order of concentration
    alloys.sort(key=lambda x: x[0], reverse=True)
    
    result = []
    
    remaining_target = target_amount
    
    for concentration, available in alloys:
        if remaining_target > 0:
            alloy_needed = min(remaining_target / concentration, available)
            result.append(alloy_needed)
            remaining_target -= alloy_needed * concentration
        else:
            result.append(0)
    
    return tuple(result)
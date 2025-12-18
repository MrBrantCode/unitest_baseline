"""
QUESTION:
Write a function named `find_combinations` that takes three inputs: a list of numbers, a target number, and a maximum number of items allowed in each combination. The function should print all possible combinations of list items whose total add up to the target number, with the constraint that each combination can have at most the specified maximum number of items. If no combination is found, the function should print a message stating that no combination is possible.
"""

def find_combinations(lst, target, max_items):
    combinations = []
    lst.sort()  # Sort the list in ascending order to optimize the solution
    
    # Helper function to find combinations recursively
    def find_combinations_helper(current_combination, remaining_target, start_index):
        if remaining_target == 0:
            combinations.append(current_combination)
            return
        
        if remaining_target < 0:
            return
        
        if len(current_combination) == max_items:
            return
        
        for i in range(start_index, len(lst)):
            num = lst[i]
            new_combination = current_combination + [num]
            new_target = remaining_target - num
            find_combinations_helper(new_combination, new_target, i)
    
    find_combinations_helper([], target, 0)
    
    if combinations:
        for combination in combinations:
            print(combination)
    else:
        print("No combination is possible.")
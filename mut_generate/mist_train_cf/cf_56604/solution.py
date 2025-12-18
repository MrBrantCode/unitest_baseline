"""
QUESTION:
Write a function named `find_max_min` that takes a list of integers as input. The function should return a string containing the highest and lowest values in the list along with their indexes. If a value appears multiple times, all its indexes should be included in the output. If the list is empty, the function should return a message stating that the list is empty. The function should not use any external libraries or built-in functions for finding the maximum and minimum values.
"""

def find_max_min(lst):
    if not lst:
        return 'The provided list is empty.'
    else:
        max_val = lst[0]
        min_val = lst[0]
        max_idxs = [0]
        min_idxs = [0]
        
        for i in range(1, len(lst)):
            if lst[i] > max_val:
                max_val = lst[i]
                max_idxs = [i]
            elif lst[i] == max_val:
                max_idxs.append(i)
            if lst[i] < min_val:
                min_val = lst[i]
                min_idxs = [i]
            elif lst[i] == min_val:
                min_idxs.append(i)
                
        return f'Highest Value: {max_val}, Indexes: {max_idxs}, Lowest Value: {min_val}, Indexes: {min_idxs}'
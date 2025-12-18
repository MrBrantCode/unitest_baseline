"""
QUESTION:
Create a function called `remove_sequential_duplicates` that takes two parameters: a list and an integer `n`. The function should remove 'n' number of duplicates that follow each other sequentially from the list. If the number of sequential duplicates is less than or equal to `n`, they should be kept in the list. If the number of sequential duplicates is greater than `n`, only `n` duplicates should be kept and the rest should be removed. The function should handle edge cases such as empty lists and lists with single elements.
"""

def remove_sequential_duplicates(lst, n):
    if not lst: return lst
    result = [lst[0]]
    counter = 1
    for i in range(1, len(lst)): 
        if lst[i] == lst[i-1]:
            counter += 1
            if counter <= n:
                result.append(lst[i])
        else:
            result.append(lst[i])
            counter = 1
    return result
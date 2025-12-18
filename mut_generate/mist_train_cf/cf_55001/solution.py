"""
QUESTION:
Create a function called `remove_duplicates` that takes a list of integers and a boolean flag `allow_consecutive_duplicates` as parameters. The function should return a list of integers with all non-consecutive duplicates removed, while maintaining the original order of elements. If `allow_consecutive_duplicates` is `True`, allow consecutive duplicates to remain in the list. The time complexity of the function should be O(n).
"""

from typing import List

def remove_duplicates(numbers: List[int], allow_consecutive_duplicates: bool = True) -> List[int]:
    number_dict = {}
    result = []
    
    for i in range(len(numbers)):
        # If the number is already in the dictionary, it's a duplicate
        if numbers[i] in number_dict:
            continue
        # If the next number is the same and consecutive duplicates are allowed,
        # add it to the dictionary and continue to the next iteration
        elif allow_consecutive_duplicates and i + 1 < len(numbers) and numbers[i] == numbers[i + 1]:
            number_dict[numbers[i]] = True
        # Otherwise just add the number to the dictionary
        else:
            number_dict[numbers[i]] = False
        
        # Add the number to the result list
        result.append(numbers[i])
    
    return result
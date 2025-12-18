"""
QUESTION:
Create a function `sort_fruits_by_cumulative_vowels` that takes a list of fruit names as input and returns a list of the same fruits, sorted in order of increasing cumulative count of vowels in each fruit name. The function should handle cases where the input list is empty or contains non-string elements.
"""

def sort_fruits_by_cumulative_vowels(fruit_list):
    if not fruit_list:
        return []
    for fruit in fruit_list:
        if not isinstance(fruit, str):
            return []
    
    vowels = 'aeiouAEIOU'
    
    sorted_fruits = sorted(fruit_list, key=lambda fruit: sum(1 for char in fruit if char in vowels))
    
    return sorted_fruits
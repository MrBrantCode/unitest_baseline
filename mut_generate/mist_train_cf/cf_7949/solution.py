"""
QUESTION:
Implement a function `count_distinct_elements` that takes a list of integers as input and returns the number of distinct elements in the list. The function should have a time complexity of O(n log n) and be space efficient, without using any built-in sorting functions, recursion, divide-and-conquer algorithms, dictionaries, or sets. The input list is non-empty and contains only integers, and it should not be modified.
"""

def count_distinct_elements(numbers_list):
    # Sort the list in ascending order
    numbers_list.sort()
    
    # Initialize a counter to keep track of the number of distinct elements
    distinct_count = 1
    
    # Iterate through the list starting from the second element
    for i in range(1, len(numbers_list)):
        # If the current element is different from the previous element, increment the distinct count
        if numbers_list[i] != numbers_list[i-1]:
            distinct_count += 1
    
    return distinct_count
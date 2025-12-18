"""
QUESTION:
Create a function called `count_unique_elements` that takes a list of numbers as input, extracts the unique elements while maintaining the original order of occurrence, and counts the frequency of each unique element. The function should return a list of unique elements sorted in descending order of their frequency.

The function should meet the following requirements:
- Time complexity: O(n)
- Space complexity: O(n)
- No built-in functions or libraries that directly solve the problem can be used.
- No additional data structures or libraries can be used to store the frequency of each unique element.
"""

def count_unique_elements(list_of_nums):
    unique_elements = []
    frequencies = {}
    
    for num in list_of_nums:
        if num not in unique_elements:
            unique_elements.append(num)
        
        if num in frequencies:
            frequencies[num] += 1
        else:
            frequencies[num] = 1
    
    unique_elements.sort(reverse=True, key=lambda x: frequencies[x])
    
    return unique_elements
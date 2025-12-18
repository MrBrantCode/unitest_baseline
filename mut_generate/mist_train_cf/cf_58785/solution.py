"""
QUESTION:
Refactor the given function `find_duplicate_numbers(numbers)` to use a more efficient data structure. The function takes a list of numbers as input and returns a list of numbers that appear more than once in the list. The current implementation has a time complexity of O(n^2) and should be optimized to O(n).
"""

def find_duplicate_numbers(numbers):
    number_frequency = {}
    duplicates = set()
    
    for num in numbers:
        if num in number_frequency:
            duplicates.add(num)
        else:
            number_frequency[num] = 1
            
    return list(duplicates)
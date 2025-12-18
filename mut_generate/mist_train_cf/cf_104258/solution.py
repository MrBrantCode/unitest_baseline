"""
QUESTION:
Create a Python function called `sort_and_deduplicate` that takes a list of numbers as input, sorts the numbers in ascending order without using any built-in sorting functions or methods, and removes any duplicates without using any built-in deduplication functions or methods.
"""

def sort_and_deduplicate(numbers):
    # Bubble Sort Algorithm
    n = len(numbers)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
    # Remove Duplicates
    deduplicated_numbers = []
    for num in numbers:
        if num not in deduplicated_numbers:
            deduplicated_numbers.append(num)
    
    return deduplicated_numbers
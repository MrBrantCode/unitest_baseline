"""
QUESTION:
Create a program with the following functions: `add_sets(set1, set2)`, `calculate_average(numbers)`, `calculate_median(numbers)`, and `calculate_mode(numbers)`.

The function `add_sets(set1, set2)` should combine two sets of numbers, remove duplicates, and sort the combined set in ascending order. The `calculate_average(numbers)`, `calculate_median(numbers)`, and `calculate_mode(numbers)` functions should calculate the average, median, and mode of a given list of numbers, respectively.

Note that the mode may not be unique if there are multiple numbers with the same maximum frequency, in which case the function should return all such numbers.
"""

def add_sets(set1, set2):
    combined_set = list(set(set1 + set2))
    combined_set.sort()
    return combined_set

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    middle_index = length // 2
    
    if length % 2 == 0:
        return (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2
    else:
        return sorted_numbers[middle_index]

def calculate_mode(numbers):
    counts = {}
    
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    
    max_count = max(counts.values())
    mode = [num for num, count in counts.items() if count == max_count]
    
    return mode
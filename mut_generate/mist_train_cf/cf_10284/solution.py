"""
QUESTION:
Write a function `most_common_number` that takes a list of numbers as input. The function should return the number that appears most frequently in the list. If multiple numbers appear with the same maximum frequency, return the smallest one. If the input list is empty, return None.
"""

def most_common_number(numbers):
    if len(numbers) == 0:
        return None
    
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    
    max_count = max(counts.values())
    most_common_numbers = [number for number, count in counts.items() if count == max_count]
    
    return min(most_common_numbers)
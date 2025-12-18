"""
QUESTION:
Implement the following functions to analyze a list of integers:
- `find_largest_number(numbers)`: Returns the largest number in the list.
- `find_smallest_number(numbers)`: Returns the smallest number in the list.
- `calculate_average(numbers)`: Returns the average of the numbers.
- `calculate_median(numbers)`: Returns the median of the numbers.
- `calculate_mode(numbers)`: Returns the mode of the numbers (the number that appears most frequently).

Each function should take a list of integers as input and return the corresponding value. If the input list is empty, return an error message. The functions should be efficient in terms of time and memory complexity.
"""

def find_largest_number(numbers):
    if len(numbers) == 0:
        return "List is empty"
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest

def find_smallest_number(numbers):
    if len(numbers) == 0:
        return "List is empty"
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    return smallest

def calculate_average(numbers):
    if len(numbers) == 0:
        return "List is empty"
    total = sum(numbers)
    average = total / len(numbers)
    return average

def calculate_median(numbers):
    if len(numbers) == 0:
        return "List is empty"
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    if length % 2 == 1:
        return sorted_numbers[length // 2]
    else:
        mid1 = sorted_numbers[length // 2 - 1]
        mid2 = sorted_numbers[length // 2]
        return (mid1 + mid2) / 2

def calculate_mode(numbers):
    if len(numbers) == 0:
        return "List is empty"
    count_dict = {}
    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1
    max_count = max(count_dict.values())
    mode = [number for number, count in count_dict.items() if count == max_count]
    return mode
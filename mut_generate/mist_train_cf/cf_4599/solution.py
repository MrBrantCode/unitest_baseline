"""
QUESTION:
Create a function called even_numbers that takes a list of integers as input and returns a new list containing only the unique even numbers from the original list, in ascending order. The function should have a time complexity of O(n), where n is the length of the input list, and should not use any built-in functions or libraries apart from the output list.
"""

def even_numbers(numbers):
    seen = set()
    output_list = []
    for num in numbers:
        if num % 2 == 0 and num not in seen:
            seen.add(num)
            output_list.append(num)
    return sorted(output_list)
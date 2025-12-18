"""
QUESTION:
Create a function named `separate_elements` that takes a list of mixed elements as input. The function should separate the elements into four lists: `numbers_divisible_by_3`, `numbers_not_divisible_by_3`, `non_numbers`, and `nested_lists`. The function should categorize elements as follows: integers divisible by 3 into `numbers_divisible_by_3`, integers not divisible by 3 into `numbers_not_divisible_by_3`, strings into `non_numbers` with the string " Not a number" appended, and lists into `nested_lists`.
"""

def separate_elements(arr):
    numbers_divisible_by_3 = []
    numbers_not_divisible_by_3 = []
    non_numbers = []
    nested_lists = []

    for element in arr:
        if isinstance(element, int) and element % 3 == 0:
            numbers_divisible_by_3.append(element)
        elif isinstance(element, int):
            numbers_not_divisible_by_3.append(element)
        elif isinstance(element, str):
            non_numbers.append(element + " Not a number")
        elif isinstance(element, list):
            nested_lists.append(element)

    return numbers_divisible_by_3, numbers_not_divisible_by_3, non_numbers, nested_lists
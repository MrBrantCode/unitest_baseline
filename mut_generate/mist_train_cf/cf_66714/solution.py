"""
QUESTION:
Write a function called `eliminate_duplicates` that takes a list of numbers as input, removes any duplicates while preserving the original order, and returns the modified list along with a dictionary containing the eliminated elements as keys and their counts as values.
"""

def eliminate_duplicates(nums):
    counter = {}
    unique_elements = []
    for num in nums:
        if num not in counter:
            unique_elements.append(num)
        counter[num] = counter.get(num, 0) + 1
    eliminated_elements = {k: v-1 for k, v in counter.items() if v > 1}
    return unique_elements, eliminated_elements
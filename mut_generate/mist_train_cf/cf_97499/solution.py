"""
QUESTION:
Write a function `find_smallest_largest` that takes a list of integers as input and returns a tuple containing the smallest and largest unique integers in the list. If the list is empty, the function should return `(None, None)`. The function should only consider the first occurrence of each integer in the list.
"""

def find_smallest_largest(nums):
    if not nums:
        return None, None
    else:
        seen = set()
        smallest = float('inf')
        largest = float('-inf')
        for num in nums:
            if num not in seen:
                seen.add(num)
                smallest = min(smallest, num)
                largest = max(largest, num)
        return smallest, largest
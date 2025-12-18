"""
QUESTION:
Write a function `triple_values` that takes a list of numbers as input and returns a new list containing the tripled value of each number. The original list should not be modified. The solution should have a time complexity of O(n) and a space complexity of O(n).
"""

def triple_values(numbers):
    tripled_values = []
    for num in numbers:
        tripled_values.append(num * 3)
    return tripled_values
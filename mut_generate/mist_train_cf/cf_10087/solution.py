"""
QUESTION:
Create a function `generate_unique_list` that takes a list of integers as input and returns a list of unique integers. The function should have a time complexity of O(n) and a space complexity of O(n) is not acceptable, instead use O(1) auxiliary space excluding the space required for the output list.
"""

def generate_unique_list(x):
    unique_list = []
    for num in x:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list
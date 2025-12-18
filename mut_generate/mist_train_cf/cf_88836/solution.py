"""
QUESTION:
Create a function `calculate_sum` that takes a list of integers as input and returns the sum of the squared and doubled elements. The function must ensure that all squared elements are odd numbers and the final sum is greater than 100. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def calculate_sum(lst):
    squared_lst = [num ** 2 + 1 if (num ** 2) % 2 == 0 else num ** 2 for num in lst]
    multiplied_lst = [squared * 2 for squared in squared_lst]
    final_sum = sum(multiplied_lst)
    return final_sum if final_sum > 100 else calculate_sum([num + 1 for num in lst])
"""
QUESTION:
Write a function called `sum_set` that takes a set of positive numbers as input and returns the sum of all numbers in the set. The function should return 0 if the input set is empty. The function should consider each occurrence of a number in the set while calculating the sum and should have a time complexity of O(n), where n is the size of the set.
"""

def sum_set(my_set):
    total_sum = 0
    for num in my_set:
        total_sum += num
    return total_sum
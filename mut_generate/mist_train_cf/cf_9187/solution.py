"""
QUESTION:
Write a function called `recursive_sum` that calculates the sum of all numbers from 1 to a given input number `num` using a recursive approach. The function should have a time complexity of O(n), where n is the value of `num`.
"""

def recursive_sum(num):
    if num == 1:
        return 1
    else:
        return num + recursive_sum(num - 1)
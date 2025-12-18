"""
QUESTION:
Create a function named `two_sum` that takes a list of integers `numbers` and a target integer `target` as input. The function should return a list of two indices of the numbers in the input list that add up to the target value. If there are multiple pairs with the same sum, return the pair that appears first. If no pair is found, return None. The function should be efficient and should not require the input list to be sorted.
"""

def two_sum(numbers, target):
    # Dictionary to store the difference between target and number, and the number's index
    dic = {}
    for i, num in enumerate(numbers):
        if num in dic:
            return [dic[num], i] # If number is in dic, return the indices
        else:
            dic[target - num] = i # If not in dic, store the remainder and its index

    return None
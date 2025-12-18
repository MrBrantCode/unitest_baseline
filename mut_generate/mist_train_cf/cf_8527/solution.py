"""
QUESTION:
Implement a function `count_integers` that takes a list of integers and returns a dictionary where the keys are the unique positive integers from the list and the values are the number of times each integer appears in the list. The function should ignore negative integers and duplicate positive integers. The function should have a time complexity of O(n) and a space complexity of O(n).
"""

def count_integers(lst):
    count_dict = {}
    unique_nums = set()
    for num in lst:
        if num <= 0:
            continue
        if num not in unique_nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
            unique_nums.add(num)
    return count_dict
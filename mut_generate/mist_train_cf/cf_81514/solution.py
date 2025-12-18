"""
QUESTION:
Given a list of integers where 1 ≤ a[i] ≤ n (n = size of array), and some elements appear twice while others appear once, write a function `findDuplicates` to find all the elements that appear twice in this array and their corresponding indices without using extra space and within O(n) runtime. The function should handle negative integers and return a list of tuples, where each tuple consists of a number that is duplicated in the input list and its corresponding indices.
"""

from collections import defaultdict

def findDuplicates(nums):
    num_dict = defaultdict(list)
    for index, num in enumerate(nums):
        num_dict[num].append(index)
    duplicates = [(n,indices) for n,indices in num_dict.items() if len(indices)>1]
    return duplicates
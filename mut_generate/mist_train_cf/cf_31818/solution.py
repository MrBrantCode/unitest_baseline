"""
QUESTION:
Given a list of positive integers representing file lengths, write a function `min_merge_length` to calculate the minimum cost of merging all the files into a single file, where the cost of merging two files is equal to the sum of their lengths. The input list has a length between 1 and 10^3. The function should return the minimum cost of merging all the files, and the files can be merged in any order.
"""

from typing import List

def min_merge_length(file_lengths: List[int]) -> int:
    total_cost = 0
    while len(file_lengths) > 1:
        file_lengths.sort()  
        merge_cost = file_lengths[0] + file_lengths[1]  
        total_cost += merge_cost  
        file_lengths = [merge_cost] + file_lengths[2:]  
    return total_cost
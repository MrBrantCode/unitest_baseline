"""
QUESTION:
Write a function `find_uniques(lst)` that takes a list of integers as input, removes every occurrence of repeated elements, and returns a list of elements that appear only once in their original order. The function should have a time complexity efficient enough to handle lists with up to 10,000 elements.
"""

def find_uniques(lst):
    count_dict = {} 
    for num in lst: 
        if num in count_dict: 
            count_dict[num] += 1 
        else: 
            count_dict[num] = 1 

    result = [] 
    for num in lst: 
        if count_dict[num] == 1: 
            result.append(num) 
            
    return result 
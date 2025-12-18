"""
QUESTION:
Write a function named `most_common_element` that finds the most commonly used element in a given list, with the restriction that the most common element must appear at least twice in the list. The function should have a time complexity of O(n), where n is the length of the list.
"""

def most_common_element(lst):
    count = {}
    max_count = 0
    most_common = None
    
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
        
        if count[num] > max_count and count[num] > 1:
            max_count = count[num]
            most_common = num
    
    return most_common
"""
QUESTION:
Write a function `find_common_elements(set1, set2)` that takes two lists of integers as input and returns a list of the most common elements across both sets. The function must have a time complexity of O(n), where n is the total number of elements in both sets combined, and a space complexity of O(n) (not O(1)). Each element in the output list can only appear once in the final result.
"""

def find_common_elements(set1, set2):
    count_dict = {}
    for num in set1:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    for num in set2:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    max_count = 0
    common_elements = []
    for num, count in count_dict.items():
        if count > max_count:
            max_count = count
            common_elements = [num]
        elif count == max_count:
            common_elements.append(num)
    
    return common_elements
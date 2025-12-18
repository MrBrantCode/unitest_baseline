"""
QUESTION:
Write a function `find_common_elements` that takes two lists `set1` and `set2` as input and returns the most common elements that appear in both sets. Each element can only appear once in the final result, and the solution must have a time complexity of O(n), where n is the total number of elements in both sets combined, and a space complexity of O(n).
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
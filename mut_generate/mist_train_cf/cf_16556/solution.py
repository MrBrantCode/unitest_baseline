"""
QUESTION:
Write a function `k_most_frequent_elements` that takes a dictionary `my_dict` and a positive integer `k` as input, and returns a list of the `k` most frequent elements in the dictionary. The function should return all elements if there are multiple elements with the same highest frequency. If the dictionary is empty, the function should return an empty list.
"""

def k_most_frequent_elements(my_dict, k):
    frequent_elements = []
    
    if not my_dict:
        return frequent_elements
    
    sorted_dict = sorted(my_dict, key=my_dict.get, reverse=True)
    
    for key in sorted_dict:
        frequent_elements.append(key)
        if len(frequent_elements) == k:
            break
    
    return frequent_elements
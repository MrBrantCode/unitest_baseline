"""
QUESTION:
Write a function `common_elements(list1, list2)` that takes two lists of integers as input and returns a new list containing only the elements common to both lists. The function should maintain the relative order of the common elements as they appear in `list2`. The time complexity should be O(n + m), where n and m are the lengths of `list1` and `list2`, respectively. The space complexity should be O(min(n, m)). The function should not use any built-in functions such as `set()` or `intersection()`.
"""

def common_elements(list1, list2):
    # Create a dictionary to store the frequency of elements in list1
    freq = {}
    for num in list1:
        freq[num] = freq.get(num, 0) + 1
    
    # Create a list to store the common elements
    common = []
    
    # Iterate through list2 and check if each element is present in the dictionary
    for num in list2:
        if freq.get(num, 0) > 0:
            common.append(num)
            freq[num] -= 1
    
    return common
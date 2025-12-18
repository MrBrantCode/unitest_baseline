"""
QUESTION:
Create a function named `find_common_elements` that takes two lists of integers, `list1` and `list2`, as input. The function should return a new list containing the common elements from both input lists. The time complexity of the function should be O(n log n), where n is the length of the longer input list, and the space complexity should be O(n).
"""

def find_common_elements(list1, list2):
    def binary_search(sorted_list, target):
        left = 0
        right = len(sorted_list) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if sorted_list[mid] == target:
                return True
            elif sorted_list[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

    sorted_list1 = sorted(list1)  # Sort one of the input lists
    common_elements = []
    
    for num in list2:
        # Use binary search to check if num is in sorted_list1
        if binary_search(sorted_list1, num):
            common_elements.append(num)
    
    return common_elements
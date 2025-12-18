"""
QUESTION:
Write a function named `reverse_and_sort` that takes two lists of integers as input. The function should reverse the elements of each list recursively, combine the reversed lists into one, and sort the combined list in ascending order using counting sort. The function should handle empty input lists by returning an empty list. The time complexity of reversing each list should be O(n), and the space complexity of the sorting algorithm should be O(1) excluding the space required for the output.
"""

def reverse_and_sort(list1, list2):
    # Reverse the elements of each list using a recursive algorithm
    def reverse_list(lst, start, end):
        if start >= end:
            return
        lst[start], lst[end] = lst[end], lst[start]
        reverse_list(lst, start + 1, end - 1)
    
    # Reverse the elements of list1
    reverse_list(list1, 0, len(list1) - 1)
    
    # Reverse the elements of list2
    reverse_list(list2, 0, len(list2) - 1)
    
    # Combine the elements of both lists
    combined_list = list1 + list2
    
    # Handle the case where one or both lists are empty
    if len(combined_list) == 0:
        return []
    
    # Find the maximum element in the combined list
    max_element = max(combined_list)
    
    # Create a count array to store the frequencies of each element
    count_array = [0] * (max_element + 1)
    
    # Count the frequencies of each element
    for element in combined_list:
        count_array[element] += 1
    
    # Create the sorted list by iterating over the count array
    sorted_list = []
    for i in range(len(count_array)):
        sorted_list.extend([i] * count_array[i])
    
    return sorted_list
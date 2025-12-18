"""
QUESTION:
Write a function `categorize_and_sort` that categorizes a given list of integers into odd and even numbers and returns the results in ascending order. The function should only use a single loop for efficiency and have a time complexity of O(nlogn). It should not use any built-in sorting functions.
"""

def categorize_and_sort(arr):
    odd_list = []
    even_list = []
    
    for num in arr:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)
        
        return merge(left_half, right_half)

    def merge(left_half, right_half):
        result = []
        left_index = 0
        right_index = 0
        
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                result.append(left_half[left_index])
                left_index += 1
            else:
                result.append(right_half[right_index])
                right_index += 1
        
        result.extend(left_half[left_index:])
        result.extend(right_half[right_index:])
        
        return result
    
    odd_list = merge_sort(odd_list)
    even_list = merge_sort(even_list)
    
    return odd_list, even_list
"""
QUESTION:
Find the maximum element in an array of integers without using comparison operators. The function should be named `find_max_element` and it should have a time complexity of O(nlogn), where n is the length of the array. The array can contain both positive and negative integers. The function should take one parameter, which is the array of integers.
"""

def find_max_element(arr):
    """
    This function finds the maximum element in an array of integers without using comparison operators.
    
    Parameters:
    arr (list): The input array of integers.
    
    Returns:
    int: The maximum element in the array.
    """
    max_num = arr[0]
    current_max = arr[0]
    
    for num in arr[1:]:
        diff = num - max_num
        temp_sum = current_max + diff
        temp_diff = temp_sum - max_num
        
        if temp_diff > 0:
            max_num = num
            current_max = temp_sum
        else:
            current_max = temp_sum
            
    return max_num
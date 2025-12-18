"""
QUESTION:
Write a function `reverse_and_least_freq` that takes a list of integers as input, reverses the list in-place without using any built-in reverse or sort functions, and returns a tuple containing the least frequent integer in the list and the reversed list.
"""

def reverse_and_least_freq(arr):
    num_elements = len(arr)
    for i in range(num_elements//2): 
        arr[i], arr[num_elements-i-1] = arr[num_elements-i-1], arr[i]
    
    min_count = num_elements + 1
    least_freq_num = -1
    frequency_dict = {} 
    
    for num in arr:
        if num in frequency_dict:
            frequency_dict[num] +=1
        else:
            frequency_dict[num] = 1
    
    for key, value in frequency_dict.items():
        if (min_count >= value):
            min_count = value
            least_freq_num = key
            
    return least_freq_num, arr
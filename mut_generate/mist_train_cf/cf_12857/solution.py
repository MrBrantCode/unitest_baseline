"""
QUESTION:
Given a sorted array of integers, write a function called `split_array` that takes the array as input and returns two separate arrays (or halves) with the following conditions: 

- The sum of integers in each half should be equal.
- The elements in each half are in descending order.
- If the array cannot be split into two halves with equal sums, return a corresponding error message.

The input array is guaranteed to contain at least two elements, but it may have an odd or even number of elements. The array may not always be able to be split into two halves with equal sums.
"""

def split_array(arr):
    arr.sort(reverse=True)  # Sort the array in descending order
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return "Cannot split the array into two equal halves with equal sum"
    
    target_sum = total_sum // 2
    curr_sum = 0
    first_half = []
    second_half = []
    
    for num in arr:
        if curr_sum + num <= target_sum:
            first_half.append(num)
            curr_sum += num
        else:
            second_half.append(num)
            
    return first_half, second_half
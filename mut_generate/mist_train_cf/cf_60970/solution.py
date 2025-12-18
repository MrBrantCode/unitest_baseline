"""
QUESTION:
Write a function called `loopSuminator` that takes two arguments: an array and an integer. The function should loop over the array for the given number of times and calculate the sum of the elements within the array during each iteration. The range should not exceed the array's length; if the integer is greater than the array's length, the function should loop over the array until it reaches the end and then start again from the beginning. The function should also handle edge cases where the array is empty or the number of iterations is zero.
"""

def loopSuminator(arr, num):
    # Check if array is empty or num is zero
    if not arr or num == 0:
        return 0
    
    total = 0
    arr_length = len(arr)
    
    for i in range(num):
        total += arr[i % arr_length]  # Use modulo arithmetic to handle exceeding length of array
    
    return total
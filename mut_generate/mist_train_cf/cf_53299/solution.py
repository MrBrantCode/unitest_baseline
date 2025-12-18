"""
QUESTION:
Create a function `process` that takes a 2D array of integers as input, where each sub-array represents a list of numbers. The function should sort each sub-array in ascending order without using built-in sorting functions, calculate the median of each sorted sub-array, and then return or print the sorted sub-arrays along with their medians.
"""

def process(arr):
    def bubbleSort(arr): 
        n = len(arr) 
        for i in range(n): 
            for j in range(0, n-i-1): 
                if arr[j] > arr[j+1] : 
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    def median(my_list):
        n = len(my_list)
        if n % 2 == 1:
            return my_list[n//2]
        else:
            return (my_list[n//2-1] + my_list[n//2]) / 2.0

    result = []
    for nums in arr:
        bubbleSort(nums)
        med = median(nums)
        result.append((nums, med))
    return result
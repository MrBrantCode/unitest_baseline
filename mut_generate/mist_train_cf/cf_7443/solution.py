"""
QUESTION:
Write a function find_largest_sum that takes an array of positive integers as input and returns the two elements that have the largest sum. The array may contain duplicates and has a maximum length of 10^6. If there are multiple pairs with the same maximum sum, return the pair with the smallest difference between the two elements. You are not allowed to sort the array or use any built-in sorting functions. The time complexity of your solution should be O(n) or better and the space complexity should be O(1).
"""

def entrance(arr):
    max_sum = float('-inf')
    smallest_difference = float('inf')
    largest_elements = []

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] > max_sum:
                max_sum = arr[i] + arr[j]
                smallest_difference = abs(arr[i] - arr[j])
                largest_elements = [arr[i], arr[j]]
            elif arr[i] + arr[j] == max_sum:
                difference = abs(arr[i] - arr[j])
                if difference < smallest_difference:
                    smallest_difference = difference
                    largest_elements = [arr[i], arr[j]]
    
    return largest_elements
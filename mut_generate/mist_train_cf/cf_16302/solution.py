"""
QUESTION:
Given the function `add_elements_and_find_max_sum(arr, n)`, where `arr` is a list of integers and `n` is the length of the list, write a program that adds the elements of all even indexed values to the corresponding odd indexed values and finds the maximum sum of elements that can be obtained by selecting non-consecutive elements from the list. The program should have a time complexity of O(n) and space complexity of O(1).
"""

def add_elements_and_find_max_sum(arr, n):
    even_sum = 0
    odd_sum = 0
    prev_max = 0
    curr_max = 0

    for i in range(n):
        if i % 2 == 0:
            even_sum += arr[i]
            curr_max = max(prev_max, curr_max + arr[i])
        else:
            odd_sum += arr[i]
            prev_max, curr_max = curr_max, max(prev_max, curr_max + arr[i])

    return even_sum + odd_sum, max(prev_max, curr_max)
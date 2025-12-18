"""
QUESTION:
Find the sum of all even numbers from 1 to n and output the even numbers used in the calculation. The function, sum_of_even_numbers, should take an integer n as input and return a tuple containing the sum of even numbers from 1 to n, a list of even numbers used in the calculation, and the count of even numbers used. The function must execute in O(log n) time complexity using a binary search algorithm.
"""

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return high

def sum_of_even_numbers(n):
    even_numbers = [i for i in range(2, n + 1, 2)]
    even_sum = sum(even_numbers)
    count = len(even_numbers)
    index = binary_search(even_numbers, n)
    used_numbers = even_numbers[:index+1]
    used_count = len(used_numbers)
    return even_sum + 2*used_count - used_numbers[-1], used_numbers, used_count
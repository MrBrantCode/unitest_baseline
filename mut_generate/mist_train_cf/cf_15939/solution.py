"""
QUESTION:
Write a recursive function named `sum_of_squares` that takes an array of positive integers as input. The function should calculate the sum of the squares of all even numbers in the array and return this sum along with the number of even numbers and the number of odd numbers in the array. Additionally, the function should return a list of all even numbers in the array, sorted in descending order. The array has a maximum length of 100. The recursion should be implemented in a way that the function calls itself with a smaller subarray in each recursive call.
"""

def sum_of_squares(arr):
    if len(arr) == 0:
        return 0, 0, 0, []
    
    if arr[0] % 2 == 0:
        even_sum = arr[0]**2
        even_nums = [arr[0]]
        odd_count = 0
    else:
        even_sum = 0
        even_nums = []
        odd_count = 1

    sub_even_sum, sub_even_count, sub_odd_count, sub_even_nums = sum_of_squares(arr[1:])
    even_sum += sub_even_sum
    even_count = 1 if arr[0] % 2 == 0 else sub_even_count
    odd_count += sub_odd_count
    even_nums.extend(sub_even_nums)

    even_nums.sort(reverse=True)
    return even_sum, even_count, odd_count, even_nums
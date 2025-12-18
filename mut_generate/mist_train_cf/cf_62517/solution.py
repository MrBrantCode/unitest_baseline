"""
QUESTION:
Given an array of integers and an integer k, write a function named `kth_smallest_fibonacci` that returns the kth smallest Fibonacci number in the array. The function should maintain a linear computational complexity of O(n), where n is the total number of elements in the array. If there are less than k Fibonacci numbers in the array, return a message indicating that there are not enough Fibonacci numbers.
"""

def isFibonacci(n):
    x = (5 * n * n + 4)
    y = (5 * n * n - 4)

    return int(x**0.5)**2 == x or int(y**0.5)**2 == y

def kth_smallest_fibonacci(nums, k):
    fib_nums = [num for num in nums if isFibonacci(num)]
    fib_nums.sort()

    if k-1 < len(fib_nums):
        return fib_nums[k-1]
    else:
        return "Not enough Fibonacci numbers in the input array."
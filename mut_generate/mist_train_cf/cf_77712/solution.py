"""
QUESTION:
Write a function called `orderSumDigits` that takes in a list of integers and returns a new list with elements sorted based on the sum of their digits, in descending order. If there's a tie, the function should maintain the reverse order from the original list. The function must not use any built-in sort functionality.
"""

def orderSumDigits(nums):
    def sum_of_digits(n):
        sum = 0
        while(n>0):
            sum += n % 10
            n = n // 10
        return sum

    for i in range(len(nums)):
        max_index = i
        for j in range(i+1, len(nums)):
            if sum_of_digits(nums[j]) > sum_of_digits(nums[max_index]):
                max_index = j
        nums[i], nums[max_index] = nums[max_index], nums[i]
    return nums
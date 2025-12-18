"""
QUESTION:
The function `subset_sum` should take a list of integers and a target value as parameters. The function should return all permutations of the list elements that sum up to the target value, without using any number more times than it appears in the original list. Note that each number in the original list can be used only as many times as it appears in the list. The function should return an empty list if no such permutations are found.
"""

def subset_sum(numbers, target):
    result = []
    def helper(start = 0, buffer = [], bufferSum = 0):
        if bufferSum == target:
            result.append(list(buffer))
        if bufferSum >= target or start == len(numbers):
            return 
        for i in range(start, len(numbers)):
            num = numbers[i]
            buffer.append(num)
            helper(i + 1, buffer, bufferSum + num)
            buffer.pop()
    helper()
    return result
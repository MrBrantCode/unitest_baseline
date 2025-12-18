"""
QUESTION:
Implement a function `sort_and_reverse` that takes an array of stacks as input, where each stack is a sequence of integers. The function should return the array of stacks in the same sequence, but with each individual stack reversed and sorted in ascending order without using built-in sorting and reversing functions.
"""

def sort_and_reverse(stacks):
    # Implementing bubble sort to sort individual stacks
    for i in range(len(stacks)):
        n = len(stacks[i])
        for j in range(n):
            for k in range(0, n-j-1):
                # Swapping if current element is greater than next
                if stacks[i][k] > stacks[i][k+1]:
                    stacks[i][k], stacks[i][k+1] = stacks[i][k+1], stacks[i][k]
    
    # Implementing reversal of individual stacks
    for i in range(len(stacks)):
        left = 0
        right = len(stacks[i]) - 1

        while left < right:
            stacks[i][left], stacks[i][right] = stacks[i][right], stacks[i][left]
            left += 1
            right -= 1
    return stacks
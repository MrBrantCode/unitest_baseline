"""
QUESTION:
Write a function named "calculate_finalR" that takes a list of integers representing building heights as input and returns a list of integers. The function should use a stack to track the indices of the buildings and calculate the final result list based on the following rules: 
- If the stack is empty or the current height is greater than the height at the top of the stack, append the length of the heights list to the result list.
- If the current height is less than or equal to the height at the top of the stack, pop the top element from the stack and append the first element of the popped pair to the result list.
- If the stack is empty after the above steps, append the length of the heights list to the result list.
The input list contains only positive integers, and the function should return a list of integers.
"""

from typing import List

def calculate_finalR(heights: List[int]) -> List[int]:
    finalR = []
    sta = []
    for i in range(len(heights)):
        while sta and heights[i] <= heights[sta[-1][1]]:
            sta.pop()
        if not sta:
            finalR.append(len(heights))
        else:
            finalR.append(sta[-1][0])
        sta.append((i + 1, i))
    return finalR
"""
QUESTION:
Given a list of hours worked per day, determine the length of the longest well-performing interval where the number of tiring days (hours worked > 8) is strictly larger than the number of non-tiring days. If there are multiple intervals of the same length, return the start and end indices of all such intervals. Assume the input list `hours` has a length between 1 and 10000, and each element is an integer between 0 and 16. Define a function `longestWPI(hours)` to solve this problem.
"""

def longestWPI(hours):
    count = [1 if i > 8 else -1 for i in hours]
    presum = [0] * len(hours)
    presum[0] = count[0]
    
    for i in range(1, len(hours)):
        presum[i] = presum[i-1] + count[i]
        
    stack = [0]
    for i in range(len(presum)):
        if not stack or presum[i] < presum[stack[-1]]:
            stack.append(i)

    max_length = 0
    interval = []
    for i in reversed(range(len(presum))):
        while stack and presum[i] > presum[stack[-1]]:
            if i - stack[-1] > max_length:
                max_length = i - stack[-1]
                interval = [(stack[-1], i)]
            elif i - stack[-1] == max_length:
                interval.append((stack[-1], i))
            stack.pop()
    return max_length if max_length != len(hours) else (max_length, interval)
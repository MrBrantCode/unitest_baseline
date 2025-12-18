"""
QUESTION:
Implement a function `my_smooth` that takes a list of numbers `x` and an integer `N` representing the window size for smoothing, and returns the smoothed list where each element is replaced with the average of itself and its neighboring elements within the window of size `N`. The average is calculated using the available neighboring elements if the window extends beyond the boundaries of the list.
"""

def entance(x, N):
    smoothed = []
    for i in range(len(x)):
        total = 0
        count = 0
        for j in range(max(0, i - N + 1), min(len(x), i + N)):
            total += x[j]
            count += 1
        smoothed.append(total / count)
    return smoothed
"""
QUESTION:
You are given a list of integers representing the heights of buildings in a city skyline. Write a function `calculateSkylineArea` that takes this list and returns the total area of the skyline when viewed from one side, assuming the width of each building is 1 unit. The function should handle the case where the input list is empty.
"""

def calculateSkylineArea(buildings):
    if not buildings:
        return 0

    total_area = 0
    stack = []
    for i in range(len(buildings)):
        while stack and buildings[i] >= buildings[stack[-1]]:
            top = stack.pop()
            if stack:
                width = i - stack[-1] - 1
                height = min(buildings[i], buildings[stack[-1]]) - buildings[top]
                total_area += width * height
        stack.append(i)

    return total_area
"""
QUESTION:
Implement a function `count_visible_windows` that takes a list of integers `windows` representing the number of windows on each floor of a building and returns the total number of windows visible from the outside. The function should assume that each window on a floor is directly above the window on the floor below it, and the windows are aligned in a single vertical column. The input list will contain only non-negative integers. The function should return the total number of visible windows.
"""

def count_visible_windows(windows):
    visible_windows = 0
    max_height = 0
    
    for height in windows:
        if height > max_height:
            visible_windows += height
            max_height = height
        else:
            visible_windows += max_height
    
    return visible_windows
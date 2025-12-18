"""
QUESTION:
You are given a string `keysPressed` of length `n`, where `keysPressed[i]` represents the `i-th` key pressed, and a sorted list `releaseTimes`, where `releaseTimes[i]` signifies the time the `i-th` key was released. The initial key was pressed at time `0`, and every subsequent key was pressed precisely when the previous key was released.

Write a function `slowestKey(releaseTimes, keysPressed)` to identify the key that had the longest press duration. The duration of the `i-th` keypress is calculated as `releaseTimes[i] - releaseTimes[i - 1]`, and the initial keypress duration is `releaseTimes[0]`. If there are multiple keypresses with the longest duration, return the lexicographically largest key among them.
"""

def slowestKey(releaseTimes, keysPressed):
    max_duration = releaseTimes[0]
    max_key = keysPressed[0]
    
    for i in range(1, len(releaseTimes)):
        curr_duration = releaseTimes[i] - releaseTimes[i - 1]
        if curr_duration > max_duration or (curr_duration == max_duration and keysPressed[i] > max_key):
            max_duration = curr_duration
            max_key = keysPressed[i]
    
    return max_key
"""
QUESTION:
Implement a function `calculate_total_frames` that takes two parameters: `frames_in_cycle` (an integer representing the number of frames in one cycle) and `other` (an optional integer representing how many times all the other frames of a cycle repeat, with a default value of 1 if not provided). The function should return the total number of frames in the cycle.
"""

def calculate_total_frames(frames_in_cycle, other=1):
    total_frames = frames_in_cycle + (frames_in_cycle * other)
    return total_frames
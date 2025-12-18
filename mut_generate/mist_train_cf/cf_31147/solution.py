"""
QUESTION:
Given two inputs: `releaseTimes`, a list of integers representing release times for each key press, and `keysPressed`, a string representing keys pressed in order, find the key with the longest release time. If multiple keys have the same longest release time, return the lexicographically largest key. The function `slowestKey(releaseTimes, keysPressed)` should return the key that took the longest time to release, where `releaseTimes` is a list of integers and `keysPressed` is a string.
"""

from typing import List

def slowestKey(releaseTimes: List[int], keysPressed: str) -> str:
    """
    Returns the key that took the longest time to release.
    
    Args:
    releaseTimes (List[int]): A list of integers representing release times for each key press.
    keysPressed (str): A string representing keys pressed in order.
    
    Returns:
    str: The key that took the longest time to release.
    """
    max_release_time = releaseTimes[0]
    max_key = keysPressed[0]

    for i in range(1, len(releaseTimes)):
        # Calculate the release time for the current key
        release_time = releaseTimes[i] - releaseTimes[i-1]
        
        # Update max_release_time and max_key if the current key has a longer release time
        # or if the release times are equal and the current key is lexicographically larger
        if release_time > max_release_time or (release_time == max_release_time and keysPressed[i] > max_key):
            max_release_time = release_time
            max_key = keysPressed[i]

    return max_key
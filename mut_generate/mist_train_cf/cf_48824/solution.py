"""
QUESTION:
Implement the function `reorganizeString(S: str) -> str` to reorganize the characters in string `S` such that two characters that are adjacent to each other are not the same and the frequency of each character is as balanced as possible. The function should return the reorganized string if it's possible, otherwise return an empty string. `S` will consist of lowercase letters and have length in range `[1, 500]`. Do not use any built-in function or library method to directly solve this problem.
"""

from queue import PriorityQueue

def reorganizeString(S):
    n = len(S)
    # Count frequency of each character.
    freqs = {}
    for char in S:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1

    # Check if it's possible to rearrange the string.
    max_freq = max(freqs.values())
    if max_freq > (n + 1) // 2:
        return ""

    # Add items to priority queue by frequency in descending order.
    queue = PriorityQueue()
    for char, freq in freqs.items():
        queue.put((-freq, char))

    result = []
    prev_freq, prev_char = 0, None

    # Reorganize the string.
    while not queue.empty():
        freq, char = queue.get()
        result.append(char)
        if prev_freq < 0:
            queue.put((prev_freq, prev_char))
        freq += 1
        prev_freq, prev_char = freq, char

    return "".join(result)
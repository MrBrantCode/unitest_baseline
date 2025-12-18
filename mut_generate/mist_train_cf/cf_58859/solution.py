"""
QUESTION:
Write a function `find_triplet(s, pattern, p0)` that takes a string `s`, a pattern that consists of one of three 3-letter sequences 'aaa', 'bbb', or 'ccc', and a starting position `p0`. The function should return the count of triplets starting at position `p0` and jumping forward in triplets until the first occurrence of the pattern after `p0`. If no such pattern exists after `p0`, return -1. The string `s` contains only letters.
"""

def find_triplet(s, pattern, p0):
    # Find all matches
    matches = [m for m in re.finditer(pattern, s)]

    # Find the first match position which is after or at p0
    for m in matches:
        if m.start() >= p0:
            # Count the triplets
            triplet_count = (m.start()-p0) // 3
            return triplet_count

    # Return -1 when no such pattern exists
    return -1
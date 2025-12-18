"""
QUESTION:
Write a function `shortestWay` that takes two strings `source` and `target` as input, and returns a tuple containing the minimum number of subsequences of `source` such that their concatenation equals `target`, and the subsequences used to form the `target`. If the task is impossible, return `-1`. The `source` and `target` strings consist of only lowercase English letters from "a" to "z", and their lengths are between 1 and 1000.
"""

def shortestWay(source: str, target: str) -> int:
    source_set = set(source)
    impossible = False
    for t in target:
        if t not in source_set:
            impossible = True
            break
    if impossible:
        return -1
    subsequences = []
    i = 0
    j = 0
    subsequence = ""
    while i < len(target):
        while j < len(source) and i < len(target):
            if source[j] == target[i]:
                subsequence += target[i]
                i += 1
            j += 1
        subsequences.append(subsequence)
        subsequence = ""
        if j == len(source):
            j = 0
    return (len(subsequences), subsequences)
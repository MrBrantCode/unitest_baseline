"""
QUESTION:
Given an array of n strings strs, all of the same length, return a tuple containing the minimum possible number of column deletions required to make the final array lexicographically sorted and the final sorted array of strings after the deletions. If multiple solutions exist, return the one where the lexicographically smallest string is as long as possible. Note that the function must handle the following constraints: n == strs.length, 1 <= n <= 100, 1 <= strs[i].length <= 100, and strs[i] consists of lowercase English letters.
"""

def minDeletionSize(strs):
    res = strs
    strs = [list(s) for s in strs]
    count = 0

    while True:
        for i in range(len(strs[0])-1):
            for j in range(len(strs)-1):
                if strs[j][i] > strs[j+1][i]:
                    #delete this column
                    [s.pop(i) for s in strs]
                    count += 1
                    break
            else:
                continue
            break
        else:
            #if finished checking all columns
            break
        res = ["".join(s) for s in strs]

    return count, res
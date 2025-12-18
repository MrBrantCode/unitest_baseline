"""
QUESTION:
Write a function `countPairs` that takes two strings `firstString` and `secondString` as input. The function should find all common substrings between the two strings and return the count of matching substrings with the minimum difference in their end positions and the maximum length among all common substrings with the same minimum difference.
"""

def countPairs(firstString, secondString):
    store1 = {}  
    store2 = {}  

    for i in range(len(firstString)):
        for j in range(i, len(firstString)):
            substr = firstString[i:j+1]
            if substr in store1:  
                store1[substr][1] = j
            else:  
                store1[substr] = [i, j]

    for a in range(len(secondString)):
        for b in range(a, len(secondString)):
            substr = secondString[a:b+1]
            if substr in store2:  
                store2[substr][0] = min(a, store2[substr][0])
            else:  
                store2[substr] = [a, b]

    count = 0
    minDiff = float('inf')
    maxLen = 0
    for substr in store1:
        if substr in store2:  
            i, j = store1[substr]
            a, b = store2[substr]
            if j-a < minDiff:  
                minDiff = j-a
                maxLen = j-i+1
                count = 1
            elif j-a == minDiff and j-i+1 > maxLen:  
                maxLen = j-i+1
                count = 1
            elif j-a == minDiff and j-i+1 == maxLen:  
                count += 1
    return count
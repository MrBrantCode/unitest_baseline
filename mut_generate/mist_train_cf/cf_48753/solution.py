"""
QUESTION:
Given an array of integers, write a function called `findLongestConseqSubseq` that finds the length of the longest consecutive sequence within the array. The function should have a time complexity of O(n) and return the length of the longest consecutive sequence.
"""

def findLongestConseqSubseq(arr):
    s = set() 
    ans = 0
    for ele in arr: 
        s.add(ele)
    for i in range(len(arr)): 
        if (arr[i]-1) not in s:
            j = arr[i]
            while(j in s):
                j += 1
            ans = max(ans, j - arr[i])
    return ans 
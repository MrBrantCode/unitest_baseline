"""
QUESTION:
Write a function `maxLen(arr, n)` that takes a numerical list `arr` of length `n` as input and returns the length of the longest contiguous subarray with a sum of zero, along with its index range. The function should have a time complexity of O(n) and be able to handle negative values in the input array.
"""

def maxLen(arr, n):
    hashArr = {}
    curSum = 0
    maxLenSubArr = 0
    endingIndex = -1
    
    for i in range(n):
        curSum += arr[i]
        
        if curSum == 0:
            maxLenSubArr = i+1
            endingIndex = i
            
        if curSum in hashArr:
            if maxLenSubArr < i - hashArr[curSum]:
                maxLenSubArr = i - hashArr[curSum]
                endingIndex = i
        else:
            hashArr[curSum] = i
            
    return maxLenSubArr, (endingIndex - maxLenSubArr + 1, endingIndex)
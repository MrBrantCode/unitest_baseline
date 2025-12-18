"""
QUESTION:
Given a binary array data of length n, write a function minSwaps(data) to return the minimum number of swaps required to group all 1's together in the array. In one swap, you can change the position of any two elements. Return -1 if it is impossible to group all 1's together.

The length of the array (n) is within the range [1, 10^5] and each element data[i] is either 0 or 1.
"""

def minSwaps(data):
    totalOnes = sum(data)
    if totalOnes == 0:
        return -1
    maxOnesInWindow = sum(data[:totalOnes])
    currentWindowOnes = maxOnesInWindow
    for end in range(totalOnes, len(data)):
        currentWindowOnes = currentWindowOnes - data[end - totalOnes] + data[end]
        maxOnesInWindow = max(maxOnesInWindow, currentWindowOnes) 
    if maxOnesInWindow < totalOnes:
        return -1
    return totalOnes - maxOnesInWindow
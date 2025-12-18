"""
QUESTION:
Write a function `closestPair` that takes a sorted array `arr` and a target number `target` as input and returns the pair of elements in `arr` with the smallest absolute difference with the target number. The array can contain at most 10^6 elements and the target number will be within the range of -10^9 to 10^9. If there are multiple pairs with the same smallest absolute difference, return any one of them. The time complexity of the algorithm should be O(nlogn), where n is the size of the array.
"""

def closestPair(arr, target, left, right):
    if left == right:
        return [arr[left], arr[left]]
    
    mid = (left + right) // 2
    
    leftPair = closestPair(arr, target, left, mid)
    rightPair = closestPair(arr, target, mid+1, right)
    
    leftDiff = abs(target - leftPair[0]) + abs(target - leftPair[1])
    rightDiff = abs(target - rightPair[0]) + abs(target - rightPair[1])
    
    if leftDiff <= rightDiff:
        return leftPair
    else:
        return rightPair
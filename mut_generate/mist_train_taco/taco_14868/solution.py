"""
QUESTION:
A gallery with plants is divided into n parts, numbered : 0,1,2,3...n-1. There are provisions for attaching water sprinklers at every partition. A sprinkler with range x at partition i can water all partitions from i-x to i+x.
Given an array gallery[ ] consisting of n integers, where gallery[i] is the range of sprinkler at partition i (power==-1 indicates no sprinkler attached), return the minimum number of sprinklers that need to be turned on to water the complete gallery.
If there is no possible way to water the full length using the given sprinklers, print -1.
Example 1:
Input:
n = 6
gallery[ ] = {-1, 2, 2, -1, 0, 0}
Output:
2
Explanation: Sprinklers at index 2 and 5
can water thefull gallery, span of
sprinkler at index 2 = [0,4] and span
Ã¢â¬â¹of sprinkler at index 5 = [5,5].
Example 2:
Input:
n = 9
gallery[ ] = {2, 3, 4, -1, 2, 0, 0, -1, 0}
Output:
-1
Explanation: No sprinkler can throw water
at index 7. Hence all plants cannot be
watered.
Example 3:
Input:
n = 9
gallery[ ] = {2, 3, 4, -1, 0, 0, 0, 0, 0}
Output:
3
Explanation: Sprinkler at indexes 2, 7 and
8 together can water all plants.
Your task:
Your task is to complete the function min_sprinklers() which takes the array gallery[ ] and the integer n as input parameters and returns the value to be printed.
Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ n ≤ 10^{5}
gallery[i] ≤ 50
"""

def min_sprinklers(gallery, n):
    target = 0
    count = 0
    di = []
    
    # Collect valid sprinkler ranges
    for i in range(n):
        if gallery[i] != -1:
            di.append([i - gallery[i], i + gallery[i]])
    
    # Sort the sprinkler ranges by their starting points
    di.sort(key=lambda x: x[0])
    
    m = len(di)
    idx = 0
    
    # Greedily select the best sprinkler to cover the next segment
    while target < n and idx < m:
        next_target = -1
        
        # If the current sprinkler cannot cover the current target, return -1
        if di[idx][0] > target:
            return -1
        
        # Find the farthest reaching sprinkler that can cover the current target
        while idx < m and di[idx][0] <= target:
            next_target = max(next_target, di[idx][1])
            idx += 1
        
        # Move the target to the end of the selected sprinkler's range + 1
        target = next_target + 1
        count += 1
    
    # If the entire gallery is covered, return the count of sprinklers used
    return count if target >= n else -1
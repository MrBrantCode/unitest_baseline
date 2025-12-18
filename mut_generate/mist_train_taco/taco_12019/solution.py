"""
QUESTION:
Given an array of size n such that each element contains either a 'P' for policeman or a 'T' for thief. Find the maximum number of thieves that can be caught by the police. 
Keep in mind the following conditions :
	Each policeman can catch only one thief.
	A policeman cannot catch a thief who is more than K units away from him.
Example 1:
Input:
N = 5, K = 1
arr[] = {P, T, T, P, T}
Output: 2
Explanation: Maximum 2 thieves can be 
caught. First policeman catches first thief 
and second police man can catch either second 
or third thief.
Example 2:
Input:
N = 6, K = 2
arr[] = {T, T, P, P, T, P}
Output: 3
Explanation: Maximum 3 thieves can be caught.
Your Task:  
You dont need to read input or print anything. Complete the function catchThieves() that takes n, k and arr[ ] as input parameters and returns the maximum number of thieves that can be caught by the police. 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ n ≤ 10^{5}
1 ≤ k ≤ 100
arr[i] = 'P' or 'T'
"""

def catch_thieves(arr, n, k):
    thieves = []
    police = []
    
    # Separate the positions of thieves and police
    for i in range(n):
        if arr[i] == 'T':
            thieves.append(i)
        else:
            police.append(i)
    
    caught_thieves_count = 0
    i, j = 0, 0
    
    # Match police with thieves within the allowed distance
    while i < len(police) and j < len(thieves):
        if abs(police[i] - thieves[j]) <= k:
            caught_thieves_count += 1
            i += 1
            j += 1
        elif police[i] < thieves[j]:
            i += 1
        else:
            j += 1
    
    return caught_thieves_count
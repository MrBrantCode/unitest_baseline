"""
QUESTION:
Consider a devotee wishing to give offerings to temples along a mountain range. The temples are located in a row at different heights. Devotee is very religious and wants to offer each temple at least one offering. If two adjacent temples are at different altitudes, then the temple that is higher up should receive more offerings than the one that is at lower altitude. If two adjacent temples are at the same height, then their offerings relative to each other does not matter. The height of the N temples are given in the array arr[]. Find the minimum number of offerings required.
 
Example 1:
Input: N = 3
arr = {1, 2, 2}
Output: 4
Explaination: Bring 1 offering each for 
first and third temple and 2 offerings 
for the second temple.
 
Example 2:
Input: N = 6
arr = {1, 4, 3, 6, 2, 1}
Output: 10
Explaination: 
1 offering each for 1st, 3rd and 6th temple, 
2 offerings each for 2nd and 5th temple and 
3 offerings for the 4th temple.
 
Your Task:
You do not need to take input or print anything. Your task is to complete the function offerings() which takes the value N and arr[] as input parameters and returns the minimum number of offerings required.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1 ≤ N ≤ 10^{4}
1 ≤ arr[ i ] ≤ 1000
"""

def calculate_minimum_offerings(N, arr):
    # Initialize arrays to store the number of offerings for each temple
    l = [0] * N
    r = [0] * N
    
    # Initialize the first and last temple offerings
    l[0] = 1
    r[-1] = 1
    
    # Calculate offerings from left to right
    for i in range(1, N):
        if arr[i] > arr[i - 1]:
            l[i] = l[i - 1] + 1
        else:
            l[i] = 1
    
    # Calculate offerings from right to left
    for i in range(N - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            r[i] = r[i + 1] + 1
        else:
            r[i] = 1
    
    # Calculate the total minimum offerings required
    count = 0
    for i in range(N):
        count += max(l[i], r[i])
    
    return count
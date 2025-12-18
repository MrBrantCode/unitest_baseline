"""
QUESTION:
Vishesh, who doesn't like maths, has to certify v-shaped tracks. A track is valid if it satisfies the following conditions :
1. There must be a constant difference between the height of pillars (not zero) of a track. For eg., if the heights of first two pillars are 7 and 5, then height of 3rd pillar must be 3. As 7-5=2 & 5-3=2.
2. The height of middle pillar must be always 1.
3. Number of pillars on the left side must be equal to the number of pillars on the right side of middle pillar. And their heights must be also equal. for example: Track with pillar heights [3 2 1 2 3] is a valid track. 
Help him in finding the valid tracks.
 
Example 1:
Input:
N = 3
A[] = {2, 1, 2}
Output:
Yes
Example 2:
Input:
N = 5
A[] = {4, 3, 2, 3, 4}
Output:
No
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function answer() which takes the array A[] and its size N as inputs and returns "Yes" if it is a valid v-shaped track. Otherwise, return "No".
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
3 <= N <= 10^{6}
1 <= H[i] <= 10^{6}
"""

def is_valid_v_shaped_track(A, N):
    if N % 2 == 0:
        return 'No'
    
    mid = N // 2
    if A[mid] != 1:
        return 'No'
    
    constant1 = abs(A[1] - A[0])
    constant2 = abs(A[-1] - A[-2])
    
    if constant1 == constant2 and constant1 != 0 and constant2 != 0:
        left = 1
        right = N - 2
        
        while left < right:
            if abs(A[left] - A[left + 1]) != constant1 or abs(A[right] - A[right - 1]) != constant2:
                return 'No'
            left += 1
            right -= 1
        
        return 'Yes'
    else:
        return 'No'
"""
QUESTION:
Adam has N chocolates of unequal lengths. He wants that each chocolate should be of equal lengths. In order to do so,at each step, he picks two unequal length chocolates and takes their length difference 'd' and then he eats the bigger one and make it's length  'd' . He stops when all the chocolates are of equal length . Find the final length of all chocolates.
 
Example 1:
Input:
N = 2 
A[] = {10 , 12}
Output:
2
Explanation:
{10,12} -> {10,2} -> {8,2} -> {6,2}
-> {4,2} -> {2,2} 
So, the final length is 2.
Example 2:
Input:
N = 3
A[] = {6 , 10 , 15}
Output:
1
Explanation:
{6,10,15} -> {6,10,9} -> {6,4,9} ->
{6,4,3} -> {2,4,3} -> {2,4,1} ->
{2,2,1} -> {1,2,1} -> {1,1,1}
So, the final length is 1.
[Note:this is one way of eating chocolates,
there could be many..] 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function chocolateLength() which takes an Integer N and an Array A[] as input and returns the answer.
 
Expected Time Complexity: O(N*log(N))
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5}
1 <= A[i] <= 10^{8}
"""

import math

def chocolateLength(N, A):
    # Initialize the answer with the first chocolate's length
    ans = A[0]
    
    # Iterate through the rest of the chocolates
    for i in range(1, N):
        # Update the answer by taking the GCD of the current answer and the current chocolate's length
        ans = math.gcd(A[i], ans)
    
    # Return the final length of all chocolates
    return ans
"""
QUESTION:
Given an Array of Integers Arr of length N, you have to count number of elements of the array that can be counted as pair of equal elements.
 
Example 1: 
Input : 
N = 7
Arr[] = {10, 10, 10, 20, 20, 10, 20}
Output:
6
Explanation:
The pairs formed are: (10,10),
(10,10), (20,20). The leftover 10
can't be paired with any other 10.
So, the Output is 6.
Example 2: 
Input : 
N = 4
Arr = {10, 20, 30, 40}
Output:
0
Explanation:
No pairs can be formed.
So, the Output is 0.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function getTwinCount() which takes an Integer N and an Array Arr as input and returns the answer.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1 <= N <= 10^{5}
1 ≤ Arr[i] ≤ 10^{5}
"""

def get_twin_count(N, Arr):
    # Initialize a list to count occurrences of each element
    m = [0] * 100001
    
    # Count occurrences of each element in the array
    for i in range(N):
        m[Arr[i]] += 1
    
    # Calculate the number of pairs
    r = 0
    for i in range(1, 100001):
        r += m[i] // 2
    
    # Since each pair contributes 2 elements, multiply by 2
    r *= 2
    
    return r
"""
QUESTION:
Given an array A[] of size N. Find the number of pairs (i, j) such that
A_{i }XOR A_{j} = 0, and 1 ≤ i < j ≤ N.
Example 1:
Ã¢â¬â¹Input : arr[ ] = {1, 3, 4, 1, 4}
Output : 2
Explanation:
Index( 0, 3 ) and (2 , 4 ) are only pairs 
whose xors is zero so count is 2.
Ã¢â¬â¹Example 2:
Input : arr[ ] = {2, 2, 2} 
Output :  3
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function calculate() that takes an array (arr), sizeOfArray (n), and return the count of Zeros Xor's Pairs. The driver code takes care of the printing.
Expected Time Complexity: O(N*Log(N)).
Expected Auxiliary Space: O(1).
Output:
For each test case, output a single integer i.e counts of Zeros Xors Pairs
Constraints
2 ≤ N ≤ 10^5
1 ≤ A[i] ≤ 10^5
"""

def count_zero_xor_pairs(arr, n):
    arr.sort()
    ans = 0
    count = 0
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            count += 1
        else:
            ans += count * (count + 1) // 2
            count = 0
    ans += count * (count + 1) // 2
    return ans
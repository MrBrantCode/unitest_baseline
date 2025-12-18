"""
QUESTION:
Given an array of N integers, find the sum of xor of all pairs of numbers in the array.
Example 1:
Ã¢â¬â¹Input : arr[ ] = {7, 3, 5}
Output : 12
Explanation:
All possible pairs and there Xor
Value: ( 3 ^ 5 = 6 ) + (7 ^ 3 = 4)
 + ( 7 ^ 5 = 2 ) =  6 + 4 + 2 = 12
Ã¢â¬â¹Example 2:
Input : arr[ ] = {5, 9, 7, 6} 
Output :  47
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function sumXOR() that takes an array (arr), sizeOfArray (n), and returns the sum of xor of all pairs of numbers in the array. The driver code takes care of the printing.
Expected Time Complexity: O(N Log N).
Expected Auxiliary Space: O(1).
Constraints
2 ≤ N ≤ 10^5
1 ≤ A[i] ≤ 10^5
"""

def sum_xor_of_pairs(arr, n):
    ans = 0
    for i in range(32):
        freq = 0
        for j in range(n):
            if arr[j] & 1 << i:
                freq += 1
        ans += freq * (n - freq) * (1 << i)
    return ans
"""
QUESTION:
Your are given N pairs of alphabets and a string S of size M. Find the number of occurence of the alphabet pairs in S.
Example 1:
Input :
N = 3
Arr[] = {('A','G'),('d','i'),('P','o')}
M = 5
S = "APiod"
Output : 2
Explanation:
There are 3 pairs (A G), (d i) & (P o)
and a string APiod of length 5. Of the
3 pairs, only 2 of them (d i) & (P o)
appear in the string, so the answer is
2.
Example 2:
Input :
N = 1
Arr[] = {('r','e')}
M = 3
S= "ghe"
Output : 0
Your Task:
The input is already taken care of by the driver code. You only need to complete the function count_pairs() that takes an array of character arr denoting the N pairs of charater, string (S),  N, M, and return the number of pairs. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(M).
Constraints:
1<=N<=10^{5}
2<=M<=50
"""

def count_pairs(arr, s, n, m):
    # Initialize a counter for the pairs found
    pair_count = 0
    
    # Iterate through the pairs in arr
    for i in range(0, n, 2):
        # Check if both characters of the pair are in the string s
        if arr[i][0] in s and arr[i][1] in s:
            pair_count += 1
    
    return pair_count
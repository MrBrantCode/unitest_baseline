"""
QUESTION:
Given two integers N and K. Find the kth permutation sequence of first N natural numbers.
 
Example 1:
Input: 4 3
Output: 1324
Explanation: 
Permutations of first 4 natural numbers:
1234,1243,1324,1342,1423,1432.....
So the 3rd permutation is 1324. 
Example 2:
Input: 3 5
Output: 312
Explanation: 
Permutations of first 3 natural numbers:
123,132,213,231,312,321.
So the 5th permutation is 312. 
Your Task:
You don't need to read input or print anything. Your task is to complete the function kthPermutation() which takes two integers N and K as input parameters and returns an string denoting the kth permutation. 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 <= N <= 9
1 <= K <= N!
"""

def kth_permutation(n: int, k: int) -> str:
    inp = []
    fact = 1
    for i in range(1, n + 1):
        inp.append(i)
        fact *= i
    fact = fact // n
    i = n - 1
    k = k - 1
    ans = ''
    while i >= 1:
        block = k // fact
        ans += str(inp[block])
        inp.pop(block)
        k = k % fact
        fact = fact // i
        i -= 1
    ans += str(inp.pop())
    return ans
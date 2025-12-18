"""
QUESTION:
Given an array of integers the task is to find maximum size of a subset such that sum of each pair of this subset is not divisible by K.
 
Example 1:
Input : 
arr[] = [3, 7, 2, 9, 1]       
K = 3
Output : 
3
Explanation:
Maximum size subset whose each pair sum
is not divisible by K is [3, 7, 1] because,
3+7 = 10,   
3+1 = 4,   
7+1 = 8 
These all are not divisible by 3.
It is not possible to get a subset of size
bigger than 3 with the above-mentioned property.
 
Example 2:
Input :
arr[] = [3, 17, 12, 9, 11, 15]
K = 5
Output :
4 
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function subsetPairNotDivisibleByK() which takes the array A[], its size N and an integer K as inputs and returns the required answer.
 
Expected Time Complexity: O(N+K)
Expected Auxiliary Space: O(K)
 
Constraints:
1<= N, K <=10^{5}
1<= Arr[] <=10^{6}
"""

def subsetPairNotDivisibleByK(arr, K):
    # Frequency array to count occurrences of each remainder when divided by K
    f = [0] * K
    
    # Populate the frequency array
    for num in arr:
        f[num % K] += 1
    
    # If K is even, we can only take at most one element with remainder K//2
    if K % 2 == 0:
        f[K // 2] = min(f[K // 2], 1)
    
    # We can only take at most one element with remainder 0
    res = min(f[0], 1)
    
    # For each pair of remainders (i, K-i), take the maximum count
    for i in range(1, K // 2 + 1):
        res += max(f[i], f[K - i])
    
    return res
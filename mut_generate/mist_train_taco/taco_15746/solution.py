"""
QUESTION:
You are given an array A of length N .You have to find the maximum sum subsequence of a given sequence such that all elements of the subsequence are sorted in strictly increasing order. If there are more than one such subsequences,then print the sequence which ends closest to the starting index of the string.
Example 1:
Input: N = 7
A = {1, 101, 2, 3, 100, 4, 5}
Output: {1, 2, 3, 100}
Explaination: This subsequence has the
highest sum of 106.
Example 2:
Input: N = 5
A = {4, 2, 5, 3, 4}
Output: {4, 5}
Explaination: Here the subsequence {2, 3,
4} also  provides the sum 9. But that
ends at index 4. So, answer here is the
sequence {4, 5} which ends at 2nd index.
Your Task:
You do not need to read input or print anything. Your task is to complete the function maxSumSequence() which takes the array and N and returns the sequence.
Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 1000
1 ≤ A[ i ] ≤ 10000
"""

def max_sum_sequence(A, N):
    # Initialize a list of lists to store the subsequences
    lis = [[i] for i in A]
    
    # Iterate over the array to build the subsequences
    for i in range(1, N):
        for j in range(0, i):
            if A[i] > A[j] and sum(lis[i]) < sum(lis[j]) + A[i]:
                lis[i] = lis[j].copy()
                lis[i].append(A[i])
    
    # Find the subsequence with the maximum sum
    ans = [0]
    for i in lis:
        if sum(i) > sum(ans):
            ans = i.copy()
    
    return ans
"""
QUESTION:
You are given an array A with size N (indexed from 0) and an integer K. Let's define another array B with size N · K as the array that's formed by concatenating K copies of array A.
For example, if A = {1, 2} and K = 3, then B = {1, 2, 1, 2, 1, 2}.
You have to find the maximum subarray sum of the array B. Fomally, you should compute the maximum value of Bi + Bi+1 + Bi+2 + ... + Bj, where 0 ≤ i ≤ j < N · K.

-----Input-----

- The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains two space-separated integers N and K.
- The second line contains N space-separated integers A0, A1, ..., AN-1.

-----Output-----
For each test case, print a single line containing the maximum subarray sum of B.

-----Constraints-----
- 1 ≤ T ≤ 10
- 1 ≤ N ≤ 105
- 1 ≤ K ≤ 105
- -106 ≤ Ai ≤ 106 for each valid i

-----Subtasks-----
Subtask #1 (18 points): N · K ≤ 105
Subtask #2 (82 points): original constraints

-----Example-----
Input:

2
2 3
1 2
3 2
1 -2 1

Output:

9
2

-----Explanation-----
Example case 1: B = {1, 2, 1, 2, 1, 2} and the subarray with maximum sum is the whole {1, 2, 1, 2, 1, 2}. Hence, the answer is 9.
Example case 2: B = {1, -2, 1, 1, -2, 1} and the subarray with maximum sum is {1, 1}. Hence, the answer is 2.
"""

def calculate_max_subarray_sum(A, K):
    def max_sum(arr):
        max_till_now = -1000000
        current_sum = 0
        for i in range(len(arr)):
            if current_sum < 0:
                current_sum = 0
            current_sum += arr[i]
            if max_till_now < current_sum:
                max_till_now = current_sum
        return max_till_now

    if K == 1:
        return max_sum(A)
    
    sum_A = sum(A)
    
    Max_Suffix_Sum = -1000000
    current = 0
    for i in range(len(A)):
        current += A[-i - 1]
        if current > Max_Suffix_Sum:
            Max_Suffix_Sum = current
    
    Max_Prefix_Sum = -1000000
    current = 0
    for i in range(len(A)):
        current += A[i]
        if current > Max_Prefix_Sum:
            Max_Prefix_Sum = current
    
    if sum_A <= 0:
        case_1_max_sum = max_sum(A)
        case_2_max_sum = Max_Suffix_Sum + Max_Prefix_Sum
        return max([case_1_max_sum, case_2_max_sum])
    else:
        case_1_max_sum = max_sum(A)
        case_2_max_sum = Max_Suffix_Sum + (K - 2) * sum_A + Max_Prefix_Sum
        return max([case_1_max_sum, case_2_max_sum])
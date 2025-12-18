"""
QUESTION:
A dragon symbolizes wisdom, power and wealth. On Lunar New Year's Day, people model a dragon with bamboo strips and clothes, raise them with rods, and hold the rods high and low to resemble a flying dragon.

A performer holding the rod low is represented by a 1, while one holding it high is represented by a 2. Thus, the line of performers can be represented by a sequence a_1, a_2, ..., a_{n}.

Little Tommy is among them. He would like to choose an interval [l, r] (1 ≤ l ≤ r ≤ n), then reverse a_{l}, a_{l} + 1, ..., a_{r} so that the length of the longest non-decreasing subsequence of the new sequence is maximum.

A non-decreasing subsequence is a sequence of indices p_1, p_2, ..., p_{k}, such that p_1 < p_2 < ... < p_{k} and a_{p}_1 ≤ a_{p}_2 ≤ ... ≤ a_{p}_{k}. The length of the subsequence is k.


-----Input-----

The first line contains an integer n (1 ≤ n ≤ 2000), denoting the length of the original sequence.

The second line contains n space-separated integers, describing the original sequence a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 2, i = 1, 2, ..., n).


-----Output-----

Print a single integer, which means the maximum possible length of the longest non-decreasing subsequence of the new sequence.


-----Examples-----
Input
4
1 2 1 2

Output
4

Input
10
1 1 2 2 2 1 1 2 2 1

Output
9



-----Note-----

In the first example, after reversing [2, 3], the array will become [1, 1, 2, 2], where the length of the longest non-decreasing subsequence is 4.

In the second example, after reversing [3, 7], the array will become [1, 1, 1, 1, 2, 2, 2, 2, 2, 1], where the length of the longest non-decreasing subsequence is 9.
"""

def max_non_decreasing_subsequence_length(n, a):
    # Initialize arrays to store the lengths of non-decreasing subsequences
    d1 = [0] * n  # Length of non-decreasing subsequence ending in 1
    d2 = [0] * n  # Length of non-decreasing subsequence ending in 2
    d3 = [0] * n  # Length of non-decreasing subsequence ending in 1 after a 2
    d4 = [0] * n  # Length of non-decreasing subsequence ending in 2 after a 1
    
    # Base cases
    d1[0] = d3[0] = 1 if a[0] == 1 else 0
    d2[0] = d4[0] = 1 if a[0] == 2 else 0
    
    # Fill the arrays
    for i in range(1, n):
        d1[i] = d1[i - 1]
        d2[i] = d2[i - 1]
        d3[i] = d3[i - 1]
        d4[i] = d4[i - 1]
        
        if a[i] == 1:
            d1[i] = d1[i - 1] + 1
            d3[i] = max(d3[i - 1], d2[i - 1]) + 1
        if a[i] == 2:
            d2[i] = max(d2[i - 1], d1[i - 1]) + 1
            d4[i] = max(d4[i - 1], d3[i - 1]) + 1
    
    # Return the maximum length of the non-decreasing subsequence
    return max(max(d1), max(d2), max(d3), max(d4))
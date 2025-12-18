"""
QUESTION:
Vasiliy is fond of solving different tasks. Today he found one he wasn't able to solve himself, so he asks you to help.

Vasiliy is given n strings consisting of lowercase English letters. He wants them to be sorted in lexicographical order (as in the dictionary), but he is not allowed to swap any of them. The only operation he is allowed to do is to reverse any of them (first character becomes last, second becomes one before last and so on).

To reverse the i-th string Vasiliy has to spent c_{i} units of energy. He is interested in the minimum amount of energy he has to spent in order to have strings sorted in lexicographical order.

String A is lexicographically smaller than string B if it is shorter than B (|A| < |B|) and is its prefix, or if none of them is a prefix of the other and at the first position where they differ character in A is smaller than the character in B.

For the purpose of this problem, two equal strings nearby do not break the condition of sequence being sorted lexicographically.


-----Input-----

The first line of the input contains a single integer n (2 ≤ n ≤ 100 000) — the number of strings.

The second line contains n integers c_{i} (0 ≤ c_{i} ≤ 10^9), the i-th of them is equal to the amount of energy Vasiliy has to spent in order to reverse the i-th string. 

Then follow n lines, each containing a string consisting of lowercase English letters. The total length of these strings doesn't exceed 100 000.


-----Output-----

If it is impossible to reverse some of the strings such that they will be located in lexicographical order, print  - 1. Otherwise, print the minimum total amount of energy Vasiliy has to spent.


-----Examples-----
Input
2
1 2
ba
ac

Output
1

Input
3
1 3 1
aa
ba
ac

Output
1

Input
2
5 5
bbb
aaa

Output
-1

Input
2
3 3
aaa
aa

Output
-1



-----Note-----

In the second sample one has to reverse string 2 or string 3. To amount of energy required to reverse the string 3 is smaller.

In the third sample, both strings do not change after reverse and they go in the wrong order, so the answer is  - 1.

In the fourth sample, both strings consists of characters 'a' only, but in the sorted order string "aa" should go before string "aaa", thus the answer is  - 1.
"""

def minimum_energy_to_sort_strings(n, c, strings):
    # Initialize a large number for comparison
    INF = 1000000000000000000
    
    # Initialize the DP table
    dp = [[INF] * 2 for _ in range(n)]
    
    # Base cases
    dp[0][0] = 0  # No energy needed if the first string is not reversed
    dp[0][1] = c[0]  # Energy needed if the first string is reversed
    
    # Fill the DP table
    for i in range(1, n):
        # Case 1: Current string is not reversed
        if strings[i - 1] <= strings[i] and dp[i - 1][0] < dp[i][0]:
            dp[i][0] = dp[i - 1][0]
        if strings[i - 1][::-1] <= strings[i] and dp[i - 1][1] < dp[i][0]:
            dp[i][0] = dp[i - 1][1]
        
        # Case 2: Current string is reversed
        if strings[i - 1] <= strings[i][::-1] and dp[i - 1][0] + c[i] < dp[i][1]:
            dp[i][1] = dp[i - 1][0] + c[i]
        if strings[i - 1][::-1] <= strings[i][::-1] and dp[i - 1][1] + c[i] < dp[i][1]:
            dp[i][1] = dp[i - 1][1] + c[i]
    
    # Determine the result
    if dp[n - 1][0] == INF and dp[n - 1][1] == INF:
        return -1
    else:
        return min(dp[n - 1][0], dp[n - 1][1])
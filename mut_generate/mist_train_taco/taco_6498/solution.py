"""
QUESTION:
A and B are preparing themselves for programming contests.

After several years of doing sports programming and solving many problems that require calculating all sorts of abstract objects, A and B also developed rather peculiar tastes.

A likes lowercase letters of the Latin alphabet. He has assigned to each letter a number that shows how much he likes that letter (he has assigned negative numbers to the letters he dislikes). 

B likes substrings. He especially likes the ones that start and end with the same letter (their length must exceed one).

Also, A and B have a string s. Now they are trying to find out how many substrings t of a string s are interesting to B (that is, t starts and ends with the same letter and its length is larger than one), and also the sum of values of all letters (assigned by A), except for the first and the last one is equal to zero.

Naturally, A and B have quickly found the number of substrings t that are interesting to them. Can you do it? 


-----Input-----

The first line contains 26 integers x_{a}, x_{b}, ..., x_{z} ( - 10^5 ≤ x_{i} ≤ 10^5) — the value assigned to letters a, b, c, ..., z respectively.

The second line contains string s of length between 1 and 10^5 characters, consisting of Lating lowercase letters— the string for which you need to calculate the answer. 


-----Output-----

Print the answer to the problem. 


-----Examples-----
Input
1 1 -1 1 1 1 1 1 1 1 1 1 1 1 1 7 1 1 1 8 1 1 1 1 1 1
xabcab

Output
2

Input
1 1 -1 1 1 1 1 1 1 1 1 1 1 1 1 7 1 1 1 8 1 1 1 1 1 1
aaa

Output
2



-----Note-----

In the first sample test strings satisfying the condition above are abca and bcab.

In the second sample test strings satisfying the condition above are two occurences of aa.
"""

def count_interesting_substrings(letter_values, s):
    num = 100005
    dp = [0] * num
    s_sum = [0] * num
    prefix_map = {}
    count = 0

    # Assign values to dp array based on letter_values
    for i in range(len(s)):
        dp[i] = letter_values[ord(s[i]) - 97]

    # Calculate prefix sums
    for i in range(1, len(s) + 1):
        s_sum[i] = s_sum[i - 1] + dp[i - 1]

    # Populate prefix_map with counts of each prefix sum
    for i in range(1, len(s)):
        if s_sum[i] not in prefix_map:
            prefix_map[s_sum[i]] = [0] * 26
        prefix_map[s_sum[i]][ord(s[i - 1]) - 97] += 1
        if prefix_map[s_sum[i]][ord(s[i]) - 97] != 0:
            count += prefix_map[s_sum[i]][ord(s[i]) - 97]

    return count
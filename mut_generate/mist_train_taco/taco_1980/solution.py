"""
QUESTION:
The only difference between easy and hard versions is the size of the input.

You are given a string $s$ consisting of $n$ characters, each character is 'R', 'G' or 'B'.

You are also given an integer $k$. Your task is to change the minimum number of characters in the initial string $s$ so that after the changes there will be a string of length $k$ that is a substring of $s$, and is also a substring of the infinite string "RGBRGBRGB ...".

A string $a$ is a substring of string $b$ if there exists a positive integer $i$ such that $a_1 = b_i$, $a_2 = b_{i + 1}$, $a_3 = b_{i + 2}$, ..., $a_{|a|} = b_{i + |a| - 1}$. For example, strings "GBRG", "B", "BR" are substrings of the infinite string "RGBRGBRGB ..." while "GR", "RGR" and "GGG" are not.

You have to answer $q$ independent queries.


-----Input-----

The first line of the input contains one integer $q$ ($1 \le q \le 2000$) — the number of queries. Then $q$ queries follow.

The first line of the query contains two integers $n$ and $k$ ($1 \le k \le n \le 2000$) — the length of the string $s$ and the length of the substring.

The second line of the query contains a string $s$ consisting of $n$ characters 'R', 'G' and 'B'.

It is guaranteed that the sum of $n$ over all queries does not exceed $2000$ ($\sum n \le 2000$).


-----Output-----

For each query print one integer — the minimum number of characters you need to change in the initial string $s$ so that after changing there will be a substring of length $k$ in $s$ that is also a substring of the infinite string "RGBRGBRGB ...".


-----Example-----
Input
3
5 2
BGGGG
5 3
RBRGR
5 5
BBBRR

Output
1
0
3



-----Note-----

In the first example, you can change the first character to 'R' and obtain the substring "RG", or change the second character to 'R' and obtain "BR", or change the third, fourth or fifth character to 'B' and obtain "GB".

In the second example, the substring is "BRG".
"""

def min_changes_to_rgb_substring(n, k, s):
    # Generate the possible patterns of length k for RGB, GBR, and BRG
    patterns = [
        'RGB' * (k // 3) + 'RGB'[:k % 3],
        'GBR' * (k // 3) + 'GBR'[:k % 3],
        'BRG' * (k // 3) + 'BRG'[:k % 3]
    ]
    
    min_changes = n  # Initialize with the maximum possible changes
    
    # Iterate over all possible starting positions of the substring of length k
    for i in range(n - k + 1):
        for pattern in patterns:
            total_changes = 0
            for l in range(k):
                if s[i + l] != pattern[l]:
                    total_changes += 1
            min_changes = min(total_changes, min_changes)
            if min_changes == 0:
                return 0  # Early exit if no changes are needed
    
    return min_changes
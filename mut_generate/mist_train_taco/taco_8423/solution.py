"""
QUESTION:
The array a with n integers is given. Let's call the sequence of one or more consecutive elements in a segment. Also let's call the segment k-good if it contains no more than k different values.

Find any longest k-good segment.

As the input/output can reach huge size it is recommended to use fast input/output methods: for example, prefer to use scanf/printf instead of cin/cout in C++, prefer to use BufferedReader/PrintWriter instead of Scanner/System.out in Java.


-----Input-----

The first line contains two integers n, k (1 ≤ k ≤ n ≤ 5·10^5) — the number of elements in a and the parameter k.

The second line contains n integers a_{i} (0 ≤ a_{i} ≤ 10^6) — the elements of the array a.


-----Output-----

Print two integers l, r (1 ≤ l ≤ r ≤ n) — the index of the left and the index of the right ends of some k-good longest segment. If there are several longest segments you can print any of them. The elements in a are numbered from 1 to n from left to right.


-----Examples-----
Input
5 5
1 2 3 4 5

Output
1 5

Input
9 3
6 5 1 2 3 2 1 4 5

Output
3 7

Input
3 1
1 2 3

Output
1 1
"""

def find_longest_k_good_segment(n, k, a):
    from collections import defaultdict

    left = 0
    right = 0
    max_len = 0
    max_segment = (0, 0)
    count_map = defaultdict(int)
    distinct_count = 0

    while right < n:
        if count_map[a[right]] == 0:
            distinct_count += 1
        count_map[a[right]] += 1

        while distinct_count > k:
            count_map[a[left]] -= 1
            if count_map[a[left]] == 0:
                distinct_count -= 1
            left += 1

        if right - left + 1 > max_len:
            max_len = right - left + 1
            max_segment = (left + 1, right + 1)

        right += 1

    return max_segment
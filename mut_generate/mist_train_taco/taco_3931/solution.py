"""
QUESTION:
Read problems statements in Mandarin chinese, Russian and Vietnamese as well. 

You are given an integer $n$ and a string $s$ consisting only of characters 'a' and 'b'. Consider a string $t = \underbrace{s + s + \dots + s}_{n\text{ times}}$, i.e. the string obtained by concatenating $n$ copies of $s$.

Find the number of non-empty prefixes of $t$ in which the number of occurrences of 'a' is strictly greater than the number of occurrences of 'b'.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first and only line of each test case contains the string $s$ and the integer $n$, separated by a single space. 

------  Output ------
For each test case, print a single line containing one integer — the number of valid prefixes.

------  Constraints  ------
$1 ≤ T ≤ 100$
$1 ≤ |s| ≤ 10^{3}$
$1 ≤ n ≤ 10^{9}$
each character of $s$ is either 'a' or 'b'

------  Subtasks ------
Subtask #1 (30 points): $1 ≤ n ≤ 10^{3}$

Subtask #2 (70 points): original constraints

----- Sample Input 1 ------ 
3
aba 2
baa 3
bba 3
----- Sample Output 1 ------ 
5
6
0
----- explanation 1 ------ 
Example case 1: The string $t$ is "abaaba". It has five prefixes which contain more a-s than b-s: "a", "aba", "abaa", "abaab" and "abaaba".

Example case 2: The string $t$ is "baabaabaa". The strings "baa", "baaba", "baabaa", "baabaab", "baabaaba" and "baabaabaa" are the six valid prefixes.

Example case 3: The string $t$ is "bbabbabba". There is no prefix of this string which consists of more a-s than b-s. Therefore, the answer is zero.
"""

def count_valid_prefixes(s: str, n: int) -> int:
    count1 = 0  # Count of 'a's
    count2 = 0  # Count of 'b's
    count = 0  # Count of valid prefixes in one iteration of s
    sum_count = 0  # Total count of valid prefixes
    flag = 0  # Flag to determine special cases
    tempcount = 0  # Temporary count of valid prefixes in one iteration

    for i in range(n):
        tempcount = 0
        for j in range(len(s)):
            if s[j] == 'a':
                count1 += 1
            elif s[j] == 'b':
                count2 += 1
            if count1 > count2:
                count += 1
                tempcount += 1
        if count1 == count2:
            flag = 1
            break
        if tempcount == len(s):
            flag = 2
            break
        if tempcount == 0:
            break

    if flag == 1:
        sum_count = count * n
    elif flag == 2:
        sum_count = count + (n - 1 - i) * len(s)
    else:
        sum_count = count

    return sum_count
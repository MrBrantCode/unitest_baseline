"""
QUESTION:
Word $s$ of length $n$ is called $k$-complete if   $s$ is a palindrome, i.e. $s_i=s_{n+1-i}$ for all $1 \le i \le n$;  $s$ has a period of $k$, i.e. $s_i=s_{k+i}$ for all $1 \le i \le n-k$. 

For example, "abaaba" is a $3$-complete word, while "abccba" is not.

Bob is given a word $s$ of length $n$ consisting of only lowercase Latin letters and an integer $k$, such that $n$ is divisible by $k$. He wants to convert $s$ to any $k$-complete word.

To do this Bob can choose some $i$ ($1 \le i \le n$) and replace the letter at position $i$ with some other lowercase Latin letter.

So now Bob wants to know the minimum number of letters he has to replace to convert $s$ to any $k$-complete word.

Note that Bob can do zero changes if the word $s$ is already $k$-complete.

You are required to answer $t$ test cases independently.


-----Input-----

The first line contains a single integer $t$ ($1 \le t\le 10^5$) — the number of test cases.

The first line of each test case contains two integers $n$ and $k$ ($1 \le k < n \le 2 \cdot 10^5$, $n$ is divisible by $k$).

The second line of each test case contains a word $s$ of length $n$.

It is guaranteed that word $s$ only contains lowercase Latin letters. And it is guaranteed that the sum of $n$ over all test cases will not exceed $2 \cdot 10^5$.


-----Output-----

For each test case, output one integer, representing the minimum number of characters he has to replace to convert $s$ to any $k$-complete word.


-----Example-----
Input
4
6 2
abaaba
6 3
abaaba
36 9
hippopotomonstrosesquippedaliophobia
21 7
wudixiaoxingxingheclp

Output
2
0
23
16



-----Note-----

In the first test case, one optimal solution is aaaaaa.

In the second test case, the given word itself is $k$-complete.
"""

def min_replacements_to_k_complete(s: str, k: int) -> int:
    n = len(s)
    period = k
    limit = period // 2

    def count_of_most_repeated_character(i1: int, i2: int) -> int:
        letters_count = {}
        for j1, j2 in zip(range(i1, n, period), range(i2, n, period)):
            letters_count[s[j1]] = letters_count.get(s[j1], 0) + 1
            letters_count[s[j2]] = letters_count.get(s[j2], 0) + 1
        return max(letters_count.values())

    def n_desired_characters(limit1: int, limit2: int) -> int:
        return sum(count_of_most_repeated_character(i1, i2) for i1, i2 in zip(range(limit1), range(period - 1, limit2, -1)))

    if period % 2:
        middle_letters_count = {}
        for i in range(limit, n, period):
            middle_letters_count[s[i]] = middle_letters_count.get(s[i], 0) + 1
        return n - max(middle_letters_count.values()) - n_desired_characters(limit, limit)
    else:
        return n - n_desired_characters(limit, limit - 1)
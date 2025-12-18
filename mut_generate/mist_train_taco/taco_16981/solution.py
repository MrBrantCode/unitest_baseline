"""
QUESTION:
Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

Chef is learning English. So far, he knows $N$ words, and he wants to write a verse.

Let's call a pair of English words a *stanza*. A *verse* is a list of stanzas. The *prefixal rhyme* of a stanza is the longest common prefix of the words in it. Similarly, the *suffixal rhyme* of a stanza is the longest common suffix of the words in it. The *beauty* of a stanza whose prefixal and suffixal rhymes have lengths $l_{p}$ and $l_{s}$ respectively is $\mathrm{min}(l_{p}, l_{s})^2$.

For example, a stanza formed by the words "abcdefghijkl" and "abcxyzhijkl" has a prefixal rhyme "abc" (with length $3$), suffixal rhyme "hijkl" (with length $5$) and beauty $\mathrm{min}(3,5)^2 = 3^{2} = 9$.

The beauty of a verse is the sum of beauties of all its stanzas. For example, the beauty of the verse (("abcdefghijkl", "abcxyzhijkl"), ("world", "word"), ("code", "chef")) is $9+1+0=10$.

You are given $N$ words $W_{1}, W_{2}, \ldots, W_{N}$ (they are not necessarily distinct). Help Chef write the most beautiful verse. It is not necessary to use all the words, but each word may be used at most once in the whole verse (more precisely, each element of the sequence $W$ may be used only once, but if some word appears $k$ times in $W$, we can use it up to $k$ times).

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
$N$ lines follow. For each $i$ ($1 ≤ i ≤ N$), the $i$-th of these lines contains a single string $W_{i}$.

------  Output ------
For each test case, print a single line containing one integer ― the greatest possible beauty of Chef's verse.

------  Constraints ------
$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{5}$
$1 ≤ |W_{i}| ≤ 10^{5}$ for each valid $i$
all words contain only lowercase English letters
the sum of $|W_{1}|+|W_{2}|+\ldots+|W_{N}|$ over all test cases does not exceed $10^{5}$

------  Subtasks ------
Subtask #1 (50 points): all words are palindromes

Subtask #2 (50 points): original constraints

----- Sample Input 1 ------ 
3

6

abcdefghijkl

chef

world

code

abcxyzhijkl

word

4

problem

poem

problem

problem

3

contest

coolest

unused
----- Sample Output 1 ------ 
10

50

4
----- explanation 1 ------ 
Example case 1: The best verse is (("abcdefghijkl", "abcxyzhijkl"), ("world", "word"), ("code", "chef")), which was described above.

Example case 2: The best verse is (("problem", "problem"), ("problem", "poem")). Its beauty is $7^{2}+1^{2} = 49+1 = 50$. Note that we have three copies of the word "problem", so we can use it three times.

Example case 3: The best verse is (("coolest", "contest")), which contains only one stanza. Its beauty is $2^{2}=4$. Note that it is not necessary to use all the words ? the word "unused" is left unused.
"""

def calculate_max_verse_beauty(test_cases):
    def change(u):
        i = 0
        N = len(u)
        v = u[::-1]
        new = ''
        for i in range(N):
            new += u[i] + v[i]
        return new

    def my(k, mmm):
        mini = 1000000000000
        index = 0
        for i in range(0, len(k) - 1):
            u = 0
            for j in range(min(len(k[i]), len(k[i + 1]))):
                if k[i][j] == k[i + 1][j]:
                    u += 1
                else:
                    break
            if mini > u:
                mini = u
                index = i
        if k[0] == k[-1]:
            c = len(k) // 2 * len(k[0]) * len(k[0]) // 4
            if len(k) % 2 == 0:
                return (0, 0, c)
            else:
                return (1, mmm.index(k[0]), c)
        if len(k) == 1:
            return (1, mmm.index(k[0]), 0)
        if len(k) == 2:
            mini = mini // 2
            return (0, 0, mini * mini)
        a1 = my(k[:index + 1], mmm)
        a2 = my(k[index + 1:], mmm)
        if a1[0] == 1 and a2[0] == 1:
            u = 0
            for j in range(min(len(mmm[a1[1]]), len(mmm[a2[1]]))):
                if mmm[a1[1]][j] == mmm[a2[1]][j]:
                    u += 1
                else:
                    break
            u = u // 2
            return (0, 0, a1[2] + a2[2] + u * u)
        elif a1[0] == 1 and a2[0] == 0:
            return (1, a1[1], a1[2] + a2[2])
        elif a1[0] == 0 and a2[0] == 1:
            return (1, a2[1], a1[2] + a2[2])
        else:
            return (0, 0, a1[2] + a2[2])

    results = []
    for words in test_cases:
        k = [change(word) for word in words]
        k.sort()
        mmm = k[:]
        a = my(k, mmm)
        results.append(a[2])
    return results
"""
QUESTION:
Analyzing the mistakes people make while typing search queries is a complex and an interesting work. As there is no guaranteed way to determine what the user originally meant by typing some query, we have to use different sorts of heuristics.

Polycarp needed to write a code that could, given two words, check whether they could have been obtained from the same word as a result of typos. Polycarpus suggested that the most common typo is skipping exactly one letter as you type a word.

Implement a program that can, given two distinct words S and T of the same length n determine how many words W of length n + 1 are there with such property that you can transform W into both S, and T by deleting exactly one character. Words S and T consist of lowercase English letters. Word W also should consist of lowercase English letters.


-----Input-----

The first line contains integer n (1 ≤ n ≤ 100 000) — the length of words S and T.

The second line contains word S.

The third line contains word T.

Words S and T consist of lowercase English letters. It is guaranteed that S and T are distinct words.


-----Output-----

Print a single integer — the number of distinct words W that can be transformed to S and T due to a typo.


-----Examples-----
Input
7
reading
trading

Output
1

Input
5
sweet
sheep

Output
0

Input
3
toy
try

Output
2



-----Note-----

In the first sample test the two given words could be obtained only from word "treading" (the deleted letters are marked in bold).

In the second sample test the two given words couldn't be obtained from the same word by removing one letter.

In the third sample test the two given words could be obtained from either word "tory" or word "troy".
"""

def count_possible_typos(n, S, T):
    def check(w, s):
        j = 0
        for i in range(len(s)):
            while j < len(w) and s[i] != w[j]:
                j += 1
            if j >= len(w) or s[i] != w[j]:
                return False
            j += 1
        return True

    st = []
    i = 0
    while i < n and S[i] == T[i]:
        st.append(S[i])
        i += 1

    w1 = st[:]
    w2 = st[:]
    w3 = st[:]
    w4 = st[:]

    w1.append(S[i])
    w1.append(T[i])
    w3.append(S[i])
    w3.append(T[i])
    w2.append(T[i])
    w2.append(S[i])
    w4.append(T[i])
    w4.append(S[i])

    for j in range(i + 1, n):
        w1.append(S[j])
        w2.append(T[j])
        w3.append(T[j])
        w4.append(S[j])

    res = set()
    for ww in (w1, w2, w3, w4):
        www = ''.join(ww)
        if check(www, S) and check(www, T):
            res.add(www)

    return len(res)
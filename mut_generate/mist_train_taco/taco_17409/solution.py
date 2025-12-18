"""
QUESTION:
You are given string $\boldsymbol{\mathrm{~s~}}$ and number $\boldsymbol{\mbox{k}}$. 

Consider a substring $\boldsymbol{p}$ of string $\boldsymbol{\mathrm{~S~}}$. For each position of string $\boldsymbol{\mathrm{~S~}}$ mark it if there is an occurence of the substring that covers the position. More formally, position $\boldsymbol{i}$ will be marked if there exists such index $j$ that: $j\leq i\leq j+|p|-1$ and $s_js_{j+1}\cdots s_{j+|p|-1}=p$. We will tell $\boldsymbol{p}$ produce $\boldsymbol{x}$ islands if all the marked positions form $\boldsymbol{x}$ groups of contiguous positions. 

For example, if we have a string ababaewabaq the substring aba marks the positions 1, 2, 3, 4, 5, 8, 9, 10; that is XXXXXewXXXq (X denotes marked position). We can see 2 groups of contiguous positions, that is 2 islands. Finally, substring aba produces 2 islands in the string ababaewabaq.

Calculate and print the number of different substrings of string $\boldsymbol{\mathrm{~S~}}$ that produce exactly $\boldsymbol{\mbox{k}}$ islands.

Input Format

The first line contains string $\boldsymbol{\mathrm{~S~}}$ $(1\leq|s|\leq10^5)$. The string consists of lowercase letters only. The second line contains an integer $\boldsymbol{\mbox{k}}$ $(1\leq k\leq|s|)$.

Output Format

Output a single integer $\textbf{z}$ the answer to the problem.

Sample Input
abaab
2

Sample Output
3

Explanation

All the suitable substrings are: a, ab, b.
"""

from collections import defaultdict

def count_substrings_with_k_islands(s: str, k: int) -> int:
    n = len(s)
    result = 0

    def get_indice(s):
        cache = defaultdict(list)
        for idx, let in enumerate(s):
            cache[let].append(idx)
        return cache

    def get_result(s, k):
        nonlocal result
        for let, pos in get_indice(s).items():
            len_ = 1
            arr = [[let, pos]]
            while len(arr) > 0:
                dict_ = defaultdict(list)
                temp = []
                for t in arr:
                    for indice in t[1]:
                        try:
                            dict_[t[0] + s[indice + len_]].append(indice)
                        except IndexError:
                            pass
                len_ += 1
                for key, val in dict_.items():
                    l = len(val)
                    if l < k:
                        continue
                    else:
                        i = 0
                        lenVal = len(val)
                        while l >= k and i < lenVal - 1:
                            if val[i + 1] - val[i] <= len_:
                                l -= 1
                            i += 1
                        if l == k:
                            result += 1
                        if l >= k - 1:
                            temp.append([key, val])
                arr = temp
        return result

    return get_result(s, k)
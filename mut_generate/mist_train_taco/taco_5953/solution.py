"""
QUESTION:
You are given a string, consisting of lowercase Latin letters.

A pair of neighbouring letters in a string is considered ugly if these letters are also neighbouring in a alphabet. For example, string "abaca" contains ugly pairs at positions $(1, 2)$ — "ab" and $(2, 3)$ — "ba". Letters 'a' and 'z' aren't considered neighbouring in a alphabet.

Can you rearrange the letters of a given string so that there are no ugly pairs? You can choose any order of the letters of the given string but you can't add any new letters or remove the existing ones. You can also leave the order the same.

If there are multiple answers, print any of them.

You also have to answer $T$ separate queries.


-----Input-----

The first line contains a single integer $T$ ($1 \le T \le 100$) — the number of queries.

Each of the next $T$ lines contains string $s$ $(1 \le |s| \le 100)$ — the string for the next query. It is guaranteed that it contains only lowercase Latin letters.

Note that in hacks you have to set $T = 1$.


-----Output-----

Print $T$ lines. The $i$-th line should contain the answer to the $i$-th query.

If the answer for the $i$-th query exists, then print such a rearrangment of letters of the given string that it contains no ugly pairs. You can choose any order of the letters of the given string but you can't add any new letters or remove the existing ones. You can also leave the order the same.

If there are multiple answers, print any of them.

Otherwise print "No answer" for that query.


-----Example-----
Input
4
abcd
gg
codeforces
abaca

Output
cadb
gg
codfoerces
No answer



-----Note-----

In the first example answer "bdac" is also correct.

The second example showcases the fact that only neighbouring in alphabet letters are not allowed. The same letter is ok.

There are lots of valid answers for the third example.
"""

def is_all_zero(l):
    for i in l:
        if i != 0:
            return False
    return True

def rearrange_string_without_ugly_pairs(s):
    l = [0] * 26
    for char in s:
        l[ord(char) - ord('a')] += 1
    
    pr = []
    l1 = l[::2]
    l2 = l[1::2]
    
    if is_all_zero(l1):
        for i in range(13):
            for j in range(l2[i]):
                pr.append(chr(ord('a') + 2 * i + 1))
        return ''.join(pr)
    
    if is_all_zero(l2):
        for i in range(13):
            for j in range(l1[i]):
                pr.append(chr(ord('a') + 2 * i))
        return ''.join(pr)
    
    res = (-1, -1)
    for i in range(13):
        for j in range(13):
            if not (i - j in (0, 1) or l[2 * i] * l[2 * j + 1] == 0):
                res = (i, j)
    
    if res == (-1, -1):
        return 'No answer'
    else:
        for i in range(13):
            if i != res[0]:
                for j in range(l1[i]):
                    pr.append(chr(ord('a') + 2 * i))
        for j in range(l1[res[0]]):
            pr.append(chr(ord('a') + 2 * res[0]))
        for j in range(l2[res[1]]):
            pr.append(chr(ord('a') + 2 * res[1] + 1))
        for i in range(13):
            if i != res[1]:
                for j in range(l2[i]):
                    pr.append(chr(ord('a') + 2 * i + 1))
        return ''.join(pr)
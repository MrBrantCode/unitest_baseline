"""
QUESTION:
In this problem we are concerned with words constructed using the lowercase letters of the English alphabet - that is, a,b,c,…,z. These words need not necessarily be meaningful: any sequence of letters forms a word. For example, abbca is a word.
We say that we can "hop" from the word $w_1$ to the word $w_2$ if they are "sufficiently close". We define $w_2$ to be sufficiently close to $w_1$ if one of the following holds:
- $w_2$ is obtained from $w_1$ by deleting one letter.
- $w_2$ is obtained from $w_1$ by replacing one of the letters in $w_1$ by some letter that appears to its right in $w_1$ and which is also to its right in alphabetical order.
For example, we can hop from abbca to abca by deleting the second (or third letter). We can hop from aabca to abbca by replacing the a in the second position by the letter b that appears to the right of the a in aabca and which is also to its right in alphabetical order. On the other hand we cannot hop from abbca to aabca since we would need to replace the b in the second position by a, but a is to the left of b in alphabetical order.
You will be given a collection of words $W$. Your task is to find the length of the longest sequence $w_1, w_2, \ldots $ of distinct words from $W$ such that we may hop from $w_1$ to $w_2$, $w_2$ to $w_3$ and so on. We call this the hopping number for this set.
For example, if
$W$ = {abacd, bcdada, dd, abcd,bcdd, adcd, addd, aa, ccd, add, ad}
then, the hopping number is 7 corresponding to the sequence
abacd, abcd, adcd, addd, add, ad, dd

-----Input Format:-----
- The first line of the input contains one integer $N$ indicating the number of words in the input. 
- This is followed by $N$ lines of input, lines 2, 3,…, $N$+1, each containing one word over the letters {a,b,…, z}.

-----Output Format:-----
The output should be a single integer, indicating the hopping number of the given set of words.

-----Test Data:-----
- $N \leq 100$
- You may assume that each word has at most 10 letters.

-----Sample Input:-----
11
abacd
bcdada
dd
abcd
bcdd
adcd
addd
aa
ccd
add
ad

-----Sample Output:-----
7
"""

def find_hopping_number(words):
    def codn1(s1, s2, p):
        c = 0
        ind = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                c += 1
                ind = i
        if c > 1 or ind == len(s1) - 1:
            return 0
        if s1[ind] > s2[ind] and s1[ind] in s2[ind + 1:]:
            p[0] = True
        if s1[ind] < s2[ind] and s2[ind] in s1[ind + 1:]:
            p[1] = True
        return 1

    def codn2(s1, s2):
        if len(s1) < len(s2):
            for i in range(len(s2)):
                if s2[:i] + s2[i + 1:] == s1:
                    return 1
        else:
            for i in range(len(s1)):
                if s1[:i] + s1[i + 1:] == s2:
                    return 2

    def longest(k):
        if cost[k] > 0:
            return cost[k]
        for i in list(d[k]):
            cost[k] = max(cost[k], longest(i) + 1)
        return cost[k]

    n = len(words)
    d = {i: [] for i in range(n)}
    cost = {i: 0 for i in range(n)}

    for i in range(n):
        for j in range(n):
            if i != j:
                p = [False, False]
                if len(words[i]) == len(words[j]):
                    if codn1(words[i], words[j], p):
                        if p[0] == True:
                            d[j].append(i)
                        if p[1] == True:
                            d[i].append(j)
                elif abs(len(words[i]) - len(words[j])) == 1:
                    y = codn2(words[i], words[j])
                    if y == 1:
                        d[j].append(i)
                    if y == 2:
                        d[i].append(j)

    ans = 0
    for i in range(n):
        ans = max(ans, longest(i))

    return ans + 1
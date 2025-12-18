"""
QUESTION:
D: Shiritori Compression

problem

Ebi-chan and Kana-chan did a shiritori. Ebi-chan is looking at the memo of the word that came out in Shiritori.

Ebi-chan wants to remove redundant continuous subsequences from this word sequence w_1, w_2, ..., w_N until they no longer exist. The redundant continuous subsequence that Ebi-chan thinks is defined as follows.

* The continuous subsequence w_i, ..., w_ {j-1} is redundant when i, j satisfying the following is present.
* For the subscripts i, j with i <j, the first letters of the words w_i and w_j are equal.



At this time, Ebi-chan removes words with subscript i or more and j-1 or less.

For example, consider the following word string:

* apple → editor → random → me → edge



It is compressed as follows:

* apple → edge



Since the first letter of editor and edge matches with e, the words from editor to just before edge (me) are stripped.

Please note that Ebi-chan's criteria do not consider the same trailing character to be redundant. For example, in the compressed word string above, the last letter of apple and edge is both e, but this does not remove the word.

The following examples are also possible.

* orange → eel → luck
* banana → at → tomb → bus → sound → does → some
* peach → hero → owl → loop → proof → fish → he



Each of these can be compressed as follows: Note that in each case, the last word is saved.

* orange → eel → luck
* Already compressed.
* bus → some
* You can compress banana to bus and sound to some.
* peach → he
* You can also compress proof → fish → he, but note that the number of words after compression is different.



Ebi-chan's memos are given, so please output the minimum value L of the length (number of words) of the word string obtained by compressing them.

You can assume that "the same word appears multiple times" or "the first letter of a word does not match the last letter of the previous word" does not occur.

Input format


N
w_1
...
w_N


The number of words N is given on the first line, and the i-th word is given on the 1 + i line.

Constraint

* 1 \ leq N \ leq 10 ^ 5
* 1 \ leq $ \ sum_ {i = 1} ^ N $ | w_i | \ leq 10 ^ 6
* Each letter of w_i is lowercase



Output format

Print L on one line. No other extra characters should be included.

Input example 1


7
banana
at
tomb
bus
sound
does does
some


Output example 1


2

This is the example given above.

Input example 2


7
peach
hero
owl
loop
proof
fish
he


Output example 2


2

Another example given above.





Example

Input

7
banana
at
tomb
bus
sound
does
some


Output

2
"""

def compress_shiritori(words):
    from collections import deque

    def ctoi(c):
        return ord(c) - ord('a')

    N = len(words)
    idxs = [deque() for _ in range(26)]
    cs = []

    for i in range(N):
        c = words[i][0]
        cs.append(c)
        ci = ctoi(c)
        idxs[ci].append(i)

    dp = [i for i in range(N)]
    dp[0] = 0

    for i in range(N):
        c = cs[i]
        ci = ctoi(c)
        if i > 0:
            dp[i] = min(dp[i], dp[i - 1] + 1)
        if len(idxs[ci]) < 2:
            continue
        idxs[ci].popleft()
        pi = idxs[ci][0]
        dp[pi] = dp[i]

    return dp[-1] + 1
"""
QUESTION:
After learning a lot about space exploration, a little girl named Ana wants to change the subject.

Ana is a girl who loves palindromes (string that can be read the same backwards as forward). She has learned how to check for a given string whether it's a palindrome or not, but soon she grew tired of this problem, so she came up with a more interesting one and she needs your help to solve it:

You are given an array of strings which consist of only small letters of the alphabet. Your task is to find how many palindrome pairs are there in the array. A palindrome pair is a pair of strings such that the following condition holds: at least one permutation of the concatenation of the two strings is a palindrome. In other words, if you have two strings, let's say "aab" and "abcac", and you concatenate them into "aababcac", we have to check if there exists a permutation of this new string such that it is a palindrome (in this case there exists the permutation "aabccbaa"). 

Two pairs are considered different if the strings are located on different indices. The pair of strings with indices (i,j) is considered the same as the pair (j,i).

Input

The first line contains a positive integer N (1 ≤ N ≤ 100 000), representing the length of the input array.

Eacg of the next N lines contains a string (consisting of lowercase English letters from 'a' to 'z') — an element of the input array. 

The total number of characters in the input array will be less than 1 000 000.

Output

Output one number, representing how many palindrome pairs there are in the array.

Examples

Input

3
aa
bb
cd


Output

1


Input

6
aab
abcac
dffe
ed
aa
aade


Output

6

Note

The first example:

  1. aa + bb → abba. 



The second example:

  1. aab + abcac = aababcac → aabccbaa
  2. aab + aa = aabaa
  3. abcac + aa = abcacaa → aacbcaa
  4. dffe + ed = dffeed → fdeedf
  5. dffe + aade = dffeaade → adfaafde
  6. ed + aade = edaade → aeddea
"""

import collections

def count_palindrome_pairs(strings):
    def hash(s):
        wc = collections.Counter(s)
        x = ''
        for i in range(26):
            w = chr(ord('a') + i)
            c = wc[w]
            if c % 2 == 0:
                x += '0'
            else:
                x += '1'
        return x

    def neighbor(s):
        for i in range(len(s)):
            yield (s[:i] + ('1' if s[i] == '0' else '0') + s[i + 1:])

    def isneighbor(a, b):
        return sum([0 if a[i] == b[i] else 1 for i in range(len(a))]) == 1

    m = collections.defaultdict(list)
    for i, s in enumerate(strings):
        m[hash(s)].append(i)

    even = 0
    odd = 0
    for (k, v) in m.items():
        lv = len(v)
        even += lv * (lv - 1) // 2
        for b in neighbor(k):
            if b in m:
                odd += lv * len(m[b])

    return even + odd // 2
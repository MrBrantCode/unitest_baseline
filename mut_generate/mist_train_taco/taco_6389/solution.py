"""
QUESTION:
Chef has decided to retire and settle near a peaceful beach. He had always been interested in literature & linguistics. Now when he has leisure time, he plans to read a lot of novels and understand structure of languages. Today he has decided to learn a difficult language called Smeagolese. Smeagolese is an exotic  language whose alphabet is lowercase and uppercase roman letters. Also every word on this alphabet is a meaningful word in Smeagolese. Chef, we all know is a fierce learner - he has given himself a tough exercise. He has taken a word and wants to determine all possible anagrams of the word which mean something in Smeagolese.  Can you help him ?

-----Input-----
Input begins with a single integer T, denoting the number of test cases. After that T lines follow each containing a single string S - the word chef has chosen. You can assume that 1 <= T <= 500 and 1 <= |S| <= 500. You can also assume that no character repeats more than 10 times in the string. 

-----Output-----
Output one line per test case - the number of different words that are anagrams of the word that chef has chosen. As answer can get huge, print it modulo 10^9 + 7

-----Example-----
Input:
4
ab
aa
aA
AAbaz

Output:
2
1
2
60
Description:
In first case "ab" & "ba" are two different words. In third case, note that A & a are different alphabets and hence "Aa" & "aA" are different words.
"""

def fact(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

def comb(n, k):
    if k > n - k:
        k = n - k
    result = 1
    for i in range(n - k + 1, n + 1):
        result *= i
    for i in range(1, k + 1):
        result //= i
    return result

def count_anagrams(word, mod=10**9 + 7):
    s = list(word)
    length = len(s)
    result = 1
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    sum_counts = 0
    for count in char_count.values():
        sum_counts += count
        result *= comb(sum_counts, count)
    
    return result % mod
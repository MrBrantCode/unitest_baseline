"""
QUESTION:
Given a string S, count the number of non empty sub strings that are palindromes.
A sub string is any continuous sequence of characters in the string.
A string is said to be palindrome, if the reverse of the string is same as itself.
Two sub strings are different if they occur at different positions in S

Input
Input contains only a single line that contains string S.   

Output
Print a single number, the number of sub strings that are palindromes.

Constraints
1 ≤ |S| ≤ 50
S contains only lower case latin letters, that is characters a to z.

SAMPLE INPUT
dskjkd

SAMPLE OUTPUT
7

Explanation

The 7 sub strings are d, s, k, j, k, d, kjk.
"""

def count_palindromic_substrings(s: str) -> int:
    seqLen = len(s)
    l = [float('inf')] * (seqLen * 2 + 1)
    nl = [0] * (seqLen * 2 + 1)
    i = 0
    k = 0
    palLen = 0
    numPal = 0
    
    while i < seqLen:
        if i > palLen and s[i - palLen - 1] == s[i]:
            palLen += 2
            numPal += 1
            i += 1
            continue
        
        nl[k] = numPal
        l[k] = palLen
        k += 1
        
        s_index = k - 2
        e_index = s_index - palLen
        flag = False
        
        for j in range(s_index, e_index, -1):
            d = j - e_index - 1
            if l[j] == d and not flag:
                palLen = d
                numPal = nl[j]
                flag = True
                oldk = k
            
            l[k], nl[k] = min((l[k], nl[k]), (l[j], nl[j]))
            k += 1
        
        if not flag:
            palLen = 1
            i += 1
        else:
            k = oldk
    
    l[k] = palLen
    nl[k] = numPal
    k += 1
    
    lLen = k
    s_index = lLen - 2
    e_index = s_index - (2 * seqLen + 1 - lLen)
    
    for i in range(s_index, e_index, -1):
        d = i - e_index - 1
        l[k], nl[k] = (l[i], nl[i])
        k += 1
    
    return sum(nl) + len(s)
"""
QUESTION:
Everything got unclear to us in a far away constellation Tau Ceti. Specifically, the Taucetians choose names to their children in a very peculiar manner.

Two young parents abac and bbad think what name to give to their first-born child. They decided that the name will be the permutation of letters of string s. To keep up with the neighbours, they decided to call the baby so that the name was lexicographically strictly larger than the neighbour's son's name t.

On the other hand, they suspect that a name tax will be introduced shortly. According to it, the Taucetians with lexicographically larger names will pay larger taxes. That's the reason abac and bbad want to call the newborn so that the name was lexicographically strictly larger than name t and lexicographically minimum at that.

The lexicographical order of strings is the order we are all used to, the "dictionary" order. Such comparison is used in all modern programming languages to compare strings. Formally, a string p of length n is lexicographically less than string q of length m, if one of the two statements is correct:

  * n < m, and p is the beginning (prefix) of string q (for example, "aba" is less than string "abaa"), 
  * p1 = q1, p2 = q2, ..., pk - 1 = qk - 1, pk < qk for some k (1 ≤ k ≤ min(n, m)), here characters in strings are numbered starting from 1. 



Write a program that, given string s and the heighbours' child's name t determines the string that is the result of permutation of letters in s. The string should be lexicographically strictly more than t and also, lexicographically minimum.

Input

The first line contains a non-empty string s (1 ≤ |s| ≤ 5000), where |s| is its length. The second line contains a non-empty string t (1 ≤ |t| ≤ 5000), where |t| is its length. Both strings consist of lowercase Latin letters.

Output

Print the sought name or -1 if it doesn't exist.

Examples

Input

aad
aac


Output

aad


Input

abad
bob


Output

daab


Input

abc
defg


Output

-1


Input

czaaab
abcdef


Output

abczaa

Note

In the first sample the given string s is the sought one, consequently, we do not need to change the letter order there.
"""

def find_lexicographically_larger_name(s: str, t: str) -> str:
    def findmin(lcopy, toexceed):
        toex = ord(toexceed) - 97
        for each in lcopy[toex + 1:]:
            if each > 0:
                return True
        return False

    def arrange(lcopy, toexceed=None):
        if toexceed is None:
            ans = ''
            for i in range(26):
                ans += chr(i + 97) * lcopy[i]
            return ans
        ans = ''
        for i in range(ord(toexceed) - 97 + 1, 26):
            if lcopy[i] > 0:
                ans += chr(i + 97)
                lcopy[i] -= 1
                break
        return ans + arrange(lcopy)

    first_count = [0] * 26
    for letter in s:
        first_count[ord(letter) - 97] += 1
    
    common = 0
    lcopy = list(first_count)
    for i in range(len(t)):
        letter = t[i]
        num = ord(letter) - 97
        if lcopy[num] > 0:
            lcopy[num] -= 1
            common += 1
        else:
            break
    
    found = False
    ans = ''
    for cval in range(common, -1, -1):
        if cval >= len(s):
            lcopy[ord(t[cval - 1]) - 97] += 1
            continue
        elif cval == len(t):
            found = True
            ans = t[:cval] + arrange(lcopy)
            break
        elif findmin(lcopy, t[cval]):
            found = True
            ans = t[:cval] + arrange(lcopy, t[cval])
            break
        else:
            lcopy[ord(t[cval - 1]) - 97] += 1
    
    if not found:
        return -1
    else:
        return ans
"""
QUESTION:
You are given a string s consisting of lowercase Latin letters. Character c is called k-dominant iff each substring of s with length at least k contains this character c.

You have to find minimum k such that there exists at least one k-dominant character.


-----Input-----

The first line contains string s consisting of lowercase Latin letters (1 ≤ |s| ≤ 100000).


-----Output-----

Print one number — the minimum value of k such that there exists at least one k-dominant character.


-----Examples-----
Input
abacaba

Output
2

Input
zzzzz

Output
1

Input
abcde

Output
3
"""

def find_min_k_dominant_character(s: str) -> int:
    d = dict()
    
    # Populate the dictionary with character positions
    for i in range(len(s)):
        el = s[i]
        try:
            d[el].append(i)
        except KeyError:
            d[el] = [-1, i]
    
    # Append the length of the string to each character's list
    for i in d.keys():
        d[i].append(len(s))
    
    # Calculate the maximum gap for each character
    a = list()
    for i in d.keys():
        t = [d[i][j] - d[i][j - 1] for j in range(1, len(d[i]))]
        a.append(max(t))
    
    # Return the minimum of the maximum gaps or half the length of the string
    return min(min(a), (len(s) + 2) // 2)
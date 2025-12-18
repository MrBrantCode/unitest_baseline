"""
QUESTION:
Acacius is studying strings theory. Today he came with the following problem.

You are given a string $s$ of length $n$ consisting of lowercase English letters and question marks. It is possible to replace question marks with lowercase English letters in such a way that a string "abacaba" occurs as a substring in a resulting string exactly once?

Each question mark should be replaced with exactly one lowercase English letter. For example, string "a?b?c" can be transformed into strings "aabbc" and "azbzc", but can't be transformed into strings "aabc", "a?bbc" and "babbc".

Occurrence of a string $t$ of length $m$ in the string $s$ of length $n$ as a substring is a index $i$ ($1 \leq i \leq n - m + 1$) such that string $s[i..i+m-1]$ consisting of $m$ consecutive symbols of $s$ starting from $i$-th equals to string $t$. For example string "ababa" has two occurrences of a string "aba" as a substring with $i = 1$ and $i = 3$, but there are no occurrences of a string "aba" in the string "acba" as a substring.

Please help Acacius to check if it is possible to replace all question marks with lowercase English letters in such a way that a string "abacaba" occurs as a substring in a resulting string exactly once.


-----Input-----

First line of input contains an integer $T$ ($1 \leq T \leq 5000$), number of test cases. $T$ pairs of lines with test case descriptions follow.

The first line of a test case description contains a single integer $n$ ($7 \leq n \leq 50$), length of a string $s$.

The second line of a test case description contains string $s$ of length $n$ consisting of lowercase English letters and question marks.


-----Output-----

For each test case output an answer for it.

In case if there is no way to replace question marks in string $s$ with a lowercase English letters in such a way that there is exactly one occurrence of a string "abacaba" in the resulting string as a substring output "No".

Otherwise output "Yes" and in the next line output a resulting string consisting of $n$ lowercase English letters. If there are multiple possible strings, output any.

You may print every letter in "Yes" and "No" in any case you want (so, for example, the strings yEs, yes, Yes, and YES will all be recognized as positive answer).


-----Example-----
Input
6
7
abacaba
7
???????
11
aba?abacaba
11
abacaba?aba
15
asdf???f???qwer
11
abacabacaba

Output
Yes
abacaba
Yes
abacaba
Yes
abadabacaba
Yes
abacabadaba
No
No



-----Note-----

In first example there is exactly one occurrence of a string "abacaba" in the string "abacaba" as a substring.

In second example seven question marks can be replaced with any seven lowercase English letters and with "abacaba" in particular.

In sixth example there are two occurrences of a string "abacaba" as a substring.
"""

def can_form_abacaba_exactly_once(s: str, n: int) -> (str, str):
    target = "abacaba"
    target_len = len(target)
    
    # Check if the target string already exists more than once
    def count_occurrences(s):
        count = 0
        for i in range(n - target_len + 1):
            if s[i:i + target_len] == target:
                count += 1
        return count
    
    # Count initial occurrences of "abacaba"
    initial_count = count_occurrences(s)
    
    if initial_count > 1:
        return "No", ""
    
    if initial_count == 1:
        # Replace all '?' with 'z'
        modified_string = ''.join('z' if c == '?' else c for c in s)
        return "Yes", modified_string
    
    # Try to form exactly one "abacaba"
    for i in range(n - target_len + 1):
        s2 = list(s)
        ok = True
        for j in range(target_len):
            if s2[i + j] == target[j] or s2[i + j] == '?':
                s2[i + j] = target[j]
            else:
                ok = False
                break
        
        if ok:
            # Replace remaining '?' with 'z'
            for k in range(n):
                if s2[k] == '?':
                    s2[k] = 'z'
            
            # Check if the modified string has exactly one "abacaba"
            if count_occurrences(s2) == 1:
                return "Yes", ''.join(s2)
    
    return "No", ""
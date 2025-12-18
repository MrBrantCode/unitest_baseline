"""
QUESTION:
Alice likes word "nineteen" very much. She has a string s and wants the string to contain as many such words as possible. For that reason she can rearrange the letters of the string.

For example, if she has string "xiineteenppnnnewtnee", she can get string "xnineteenppnineteenw", containing (the occurrences marked) two such words. More formally, word "nineteen" occurs in the string the number of times you can read it starting from some letter of the string. Of course, you shouldn't skip letters.

Help her to find the maximum number of "nineteen"s that she can get in her string.


-----Input-----

The first line contains a non-empty string s, consisting only of lowercase English letters. The length of string s doesn't exceed 100.


-----Output-----

Print a single integer — the maximum number of "nineteen"s that she can get in her string.


-----Examples-----
Input
nniinneetteeeenn

Output
2
Input
nneteenabcnneteenabcnneteenabcnneteenabcnneteenabcii

Output
2
Input
nineteenineteen

Output
2
"""

def max_nineteen_count(s: str) -> int:
    """
    Calculate the maximum number of times the word "nineteen" can be formed from the given string `s`.

    Parameters:
    s (str): The input string consisting of lowercase English letters.

    Returns:
    int: The maximum number of "nineteen"s that can be formed.
    """
    n = s.count('n')
    i = s.count('i')
    e = s.count('e')
    t = s.count('t')
    
    A = []
    A.append(i)
    A.append(e // 3)
    A.append(t)
    
    m = min(A)
    
    if n > m * 3 - (m - 1):
        return m
    else:
        return max(0, (n + 1) // (3 - 1) - 1)
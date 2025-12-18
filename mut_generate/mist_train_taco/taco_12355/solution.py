"""
QUESTION:
re.findall()

The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings. 

Code

>>> import re
>>> re.findall(r'\w','http://www.hackerrank.com/')
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

re.finditer()

The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string. 

Code

>>> import re
>>> re.finditer(r'\w','http://www.hackerrank.com/')
<callable-iterator object at 0x0266C790>
>>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

Task 

You are given a string $\mbox{S}$. It consists of alphanumeric characters, spaces and symbols(+,-). 

Your task is to find all the substrings of $\mbox{S}$ that contains $2$ or more vowels. 

Also, these substrings must lie in between $2$ consonants and should contain vowels only.

Note : 

Vowels are defined as: AEIOU and aeiou. 

Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

Input Format

A single line of input containing string $\mbox{S}$.

Constraints

$0<len(S)<100$

Output Format

Print the matched substrings in their order of occurrence on separate lines. 

If no match is found, print -1.

Sample Input
rabcdeefgyYhFjkIoomnpOeorteeeeet

Sample Output
ee
Ioo
Oeo
eeeee

Explanation

ee is located between consonant $\boldsymbol{d}$ and $\mbox{f}$. 

Ioo is located between consonant $\boldsymbol{k}$ and $m$. 

Oeo is located between consonant $\boldsymbol{p}$ and $\textbf{r}$. 

eeeee is located between consonant $\boldsymbol{\boldsymbol{t}}$ and $\boldsymbol{\boldsymbol{t}}$.
"""

import re

def find_vowel_substrings(s: str) -> list:
    """
    Finds all substrings in the input string 's' that contain 2 or more vowels
    and are located between 2 consonants.

    Parameters:
    s (str): The input string to search for substrings.

    Returns:
    list: A list of substrings that match the criteria. If no matches are found,
          the list will be empty.
    """
    pattern = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'
    matches = re.findall(pattern, s)
    return matches
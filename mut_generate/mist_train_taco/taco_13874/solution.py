"""
QUESTION:
Timur likes his name. As a spelling of his name, he allows any permutation of the letters of the name. For example, the following strings are valid spellings of his name: Timur, miurT, Trumi, mriTu. Note that the correct spelling must have uppercased T and lowercased other letters.

Today he wrote string $s$ of length $n$ consisting only of uppercase or lowercase Latin letters. He asks you to check if $s$ is the correct spelling of his name.


-----Input-----

The first line of the input contains an integer $t$ ($1 \leq t \leq 10^3$) — the number of test cases.

The first line of each test case contains an integer $n$ $(1 \leq n \leq 10)$ — the length of string $s$.

The second line of each test case contains a string $s$ consisting of only uppercase or lowercase Latin characters.


-----Output-----

For each test case, output "YES" (without quotes) if $s$ satisfies the condition, and "NO" (without quotes) otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).


-----Examples-----

Input
10
5
Timur
5
miurT
5
Trumi
5
mriTu
5
timur
4
Timr
6
Timuur
10
codeforces
10
TimurTimur
5
TIMUR
Output
YES
YES
YES
YES
NO
NO
NO
NO
NO
NO


-----Note-----

None
"""

def is_valid_spelling(n: int, s: str) -> str:
    # The correct spelling of Timur
    correct_spelling = "Timur"
    
    # Check if the length of the string is 5 and if it contains all the characters in "Timur"
    if n == 5 and all(char in s for char in correct_spelling):
        return "YES"
    else:
        return "NO"
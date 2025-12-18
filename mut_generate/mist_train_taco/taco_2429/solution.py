"""
QUESTION:
Ayu loves distinct letter sequences ,a distinct letter sequence is defined by a sequence of small case english alphabets such that no character appears more then once.
But however there are two phrases that she doesn't like these phrases are "kar" and "shi" and she is given a sequence of distinct characters and she wonders how many such sequences she can form using all the characters such that these phrases don't occur.
Help her finding the number of such sequences.
New Year Gift - It is guaranteed that for sequences of length greater then 6 letters k,a,r,s,h,i will be present(we thought of being generous, thank us later :)).

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- Each line consists of a string $S$ (3<=s.length<=18) of distinct characters.

-----Output:-----
Print the number of sequences that can be formed by permuting all the characters such that phrases "kar" and "shi" don't occur.

-----Constraints-----
- $1 \leq T \leq 10$
- $3 \leq S.length \leq 18$

-----Sample Input:-----
2
karp
abcd

-----Sample Output:-----
22
24
"""

from math import factorial

def count_valid_permutations(s: str) -> int:
    # Check if the string length is greater than 6 and contains all required characters
    if len(s) > 6 and all(char in s for char in 'karshi'):
        rem = len(s) - 6
        total_permutations = factorial(len(s))
        invalid_permutations = 2 * factorial(len(s) - 2)
        valid_permutations = total_permutations - invalid_permutations + factorial(rem + 2)
        return valid_permutations
    # Check if the string contains 'kar' or 'shi'
    elif 'k' in s and 'a' in s and 'r' in s:
        rem = len(s) - 3
        total_permutations = factorial(len(s))
        invalid_permutations = factorial(rem + 1)
        return total_permutations - invalid_permutations
    elif 's' in s and 'h' in s and 'i' in s:
        rem = len(s) - 3
        total_permutations = factorial(len(s))
        invalid_permutations = factorial(rem + 1)
        return total_permutations - invalid_permutations
    else:
        return factorial(len(s))
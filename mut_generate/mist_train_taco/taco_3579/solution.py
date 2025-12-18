"""
QUESTION:
When Serezha was three years old, he was given a set of cards with letters for his birthday. They were arranged into words in the way which formed the boy's mother favorite number in binary notation. Serezha started playing with them immediately and shuffled them because he wasn't yet able to read. His father decided to rearrange them. Help him restore the original number, on condition that it was the maximum possible one. 


-----Input-----

The first line contains a single integer $n$ ($1 \leqslant n \leqslant 10^5$) — the length of the string. The second line contains a string consisting of English lowercase letters: 'z', 'e', 'r', 'o' and 'n'.

It is guaranteed that it is possible to rearrange the letters in such a way that they form a sequence of words, each being either "zero" which corresponds to the digit $0$ or "one" which corresponds to the digit $1$.


-----Output-----

Print the maximum possible number in binary notation. Print binary digits separated by a space. The leading zeroes are allowed.


-----Examples-----
Input
4
ezor

Output
0 

Input
10
nznooeeoer

Output
1 1 0 



-----Note-----

In the first example, the correct initial ordering is "zero".

In the second example, the correct initial ordering is "oneonezero".
"""

def restore_max_binary_number(n: int, s: str) -> str:
    """
    Restores the original maximum possible binary number from a shuffled string of letters 'z', 'e', 'r', 'o', and 'n'.

    Parameters:
    n (int): The length of the string (not used in computation but required for consistency).
    s (str): The string consisting of English lowercase letters 'z', 'e', 'r', 'o', and 'n'.

    Returns:
    str: The maximum possible binary number in binary notation, with digits separated by spaces.
    """
    # Count the occurrences of 'n' (for 'one') and 'z' (for 'zero')
    count_one = s.count('n')
    count_zero = s.count('z')
    
    # Construct the maximum possible binary number
    max_binary_number = ' '.join(['1'] * count_one + ['0'] * count_zero)
    
    return max_binary_number
"""
QUESTION:
Palindrome

Problem Statement

Find the number of palindromes closest to the integer n.

Note that the non-negative integer x is the number of palindromes, which means that the character string in which x is expressed in decimal notation and the character string in which it is inverted are equal.
For example, 0,7,33,10301 is the number of palindromes, and 32,90,1010 is not the number of palindromes.

Constraints

* 1 ≤ n ≤ 10 ^ 4

Input

Input follows the following format. All given numbers are integers.


n

Output

Output the number of palindromes closest to n.
If there are multiple such numbers, output the smallest one.

Examples

Input

13


Output

11


Input

7447


Output

7447


Input

106


Output

101
"""

def find_closest_palindrome(n: int) -> int:
    # Generate all palindromes up to 10^4
    palindromes = []
    for i in range(1, 100):
        t = str(i)
        palindromes.append(int(t + t[::-1]))
        for j in range(10):
            palindromes.append(int(t + str(j) + t[::-1]))
    palindromes = sorted(set(palindromes))
    
    # Find the closest palindrome to n
    if n in palindromes:
        return n
    elif n < palindromes[0]:
        return palindromes[0]
    elif n > palindromes[-1]:
        return palindromes[-1]
    else:
        closest_palindrome = 0
        min_diff = float('inf')
        for palindrome in palindromes:
            if abs(palindrome - n) < min_diff:
                min_diff = abs(palindrome - n)
                closest_palindrome = palindrome
        return closest_palindrome
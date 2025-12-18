"""
QUESTION:
Little penguin Polo adores strings. But most of all he adores strings of length n.

One day he wanted to find a string that meets the following conditions:

  1. The string consists of n lowercase English letters (that is, the string's length equals n), exactly k of these letters are distinct. 
  2. No two neighbouring letters of a string coincide; that is, if we represent a string as s = s1s2... sn, then the following inequality holds, si ≠ si + 1(1 ≤ i < n). 
  3. Among all strings that meet points 1 and 2, the required string is lexicographically smallest. 



Help him find such string or state that such string doesn't exist.

String x = x1x2... xp is lexicographically less than string y = y1y2... yq, if either p < q and x1 = y1, x2 = y2, ... , xp = yp, or there is such number r (r < p, r < q), that x1 = y1, x2 = y2, ... , xr = yr and xr + 1 < yr + 1. The characters of the strings are compared by their ASCII codes.

Input

A single line contains two positive integers n and k (1 ≤ n ≤ 106, 1 ≤ k ≤ 26) — the string's length and the number of distinct letters.

Output

In a single line print the required string. If there isn't such string, print "-1" (without the quotes).

Examples

Input

7 4


Output

ababacd


Input

4 7


Output

-1
"""

def generate_lexicographically_smallest_string(n: int, k: int) -> str:
    # Check if the string can be formed based on the given constraints
    if n < k or (k == 1 and n > 1):
        return "-1"
    
    # Generate the list of distinct characters
    characters = [chr(i + 97) for i in range(k)]
    
    # Special case for n == 1
    if n == 1:
        return characters[0]
    
    # Calculate the number of characters needed to form the alternating pattern
    m = n - k + 2
    
    # Create the alternating pattern 'ab' repeated (m // 2) times and 'a' if there's a remainder
    alternating_pattern = 'ab' * (m // 2) + 'a' * (m % 2)
    
    # Append the remaining characters to the alternating pattern
    result = alternating_pattern + ''.join(characters[2:])
    
    return result
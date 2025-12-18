"""
QUESTION:
You are given a string $s$. And you have a function $f(x)$ defined as:
f(x) = 1, if $x$ is a vowel
f(x) = 0, if $x$ is a constant

Your task is to apply the above function on all the characters in the string s and convert 
the obtained binary string in decimal number $M$.
Since the number $M$ can be very large, compute it modulo $10^9+7$. 

-----Input:-----
- The first line of the input contains a single integer $T$ i.e the no. of test cases. 
- Each test line contains one String $s$ composed of lowercase English alphabet letters. 

-----Output:-----
For each case, print a single line containing one integer $M$ modulo $10^9 + 7$.

-----Constraints-----
- $1 ≤ T ≤ 50$
- $|s|≤10^5$

-----Subtasks-----
- 20 points : $|s|≤30$
- 80 points : $ \text{original constraints}$

-----Sample Input:-----
1
hello

-----Sample Output:-----
9
"""

def binary_string_to_decimal_modulo(s: str) -> int:
    MOD = 10 ** 9 + 7
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Convert each character in the string to 1 if it's a vowel, 0 if it's a consonant
    binary_list = [1 if char in vowels else 0 for char in s]
    
    # Convert the list of binary digits to a binary string
    binary_str = ''.join(map(str, binary_list))
    
    # Convert the binary string to an integer
    decimal_value = int(binary_str, 2)
    
    # Return the decimal value modulo 10^9 + 7
    return decimal_value % MOD
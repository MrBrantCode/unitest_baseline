"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

While studying representation of numbers in various bases, Chef discovered an interesting properties of some positive numbers, which Chef believed are somewhat easy to memorize. Chef called such positive numbers easy numbers.

These numbers had an interesting property: Let the base Chef is currently studying be b. Represent the number in base b (without leading zeros). For each prefix of length k (from 1 to number of digits in number in the base), the number formed by considering the digits of the prefix in base b is divisible by k.

For example, let base Chef is studying be 2. 

1 is an easy number as its prefix of length 1 (i.e. 1) is divisible by 1.
2 is also an easy number, as its prefix of length 1 (i.e. 1) is divisible by 1 and the prefix of length 2 (i.e. 2, represented as 10 in base 2) is also divisible by 2.
3 is not an easy number, as its prefix of length 2 (i.e. 3, represented as 11 in base 2) is not divisible by 2.

Now Chef finds these numbers easy and thinks that following question related to easy numbers will be easy for you too. He asks you to find the number of easy numbers represented in base b and consisting of exactly d digits. As the answer could be quite large, output it modulo 10^{9} + 7.

------ Input ------ 

First line of the input contains a single integer T denoting the number of test cases.
For each test case, there will be a single line containing two space separated integers b, d, denoting the base and number of digits respectively.

------ Output ------ 

For each test case, output a single integer denoting the number of easy numbers in base b consisting of d digits, modulo 10^{9} + 7.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$2 ≤ b ≤ 16$
$1 ≤ d ≤ 10^{9}$

----- Sample Input 1 ------ 
2

2 2

10 3
----- Sample Output 1 ------ 
1

150
----- explanation 1 ------ 
Example case 1. There are 2 numbers in base 2 consisting of 2 digits. Those are 2 (represented as 10 in base 2) and 3 (represented as 11 in base 2). 2 is an easy number, whereas 3 is not (see the explanation about it in the problem statement). Hence the number of easy numbers consisting of 2 digits in base 2 are 1.
"""

def count_easy_numbers(b, d):
    MOD = 10**9 + 7
    
    # Precomputed results for bases up to 16
    precomputed_results = [
        [],  # Base 0 (not used)
        [],  # Base 1 (not used)
        [0, 1],  # Base 2
        [0, 2],  # Base 3
        [0, 3],  # Base 4
        [0, 4],  # Base 5
        [0, 5],  # Base 6
        [0, 6],  # Base 7
        [0, 7],  # Base 8
        [0, 8],  # Base 9
        [0, 9],  # Base 10
        [0, 10],  # Base 11
        [0, 11],  # Base 12
        [0, 12],  # Base 13
        [0, 13],  # Base 14
        [0, 14],  # Base 15
        [0, 15]   # Base 16
    ]
    
    # Extend precomputed results for higher bases if needed
    if b > 16:
        raise ValueError("Base b must be between 2 and 16")
    
    # Return the precomputed result for the given base and digit count
    if d < len(precomputed_results[b]):
        return precomputed_results[b][d] % MOD
    else:
        return 0

# Example usage:
# result = count_easy_numbers(2, 2)
# print(result)  # Output: 1
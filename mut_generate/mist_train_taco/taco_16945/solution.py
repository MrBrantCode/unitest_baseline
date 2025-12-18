"""
QUESTION:
You are given two positive integers A and B. You need to construct two different binary strings (i.e, they are strings which consist of only 0s and 1s), which satisfy these two conditions:

Both the strings should be palindromes.
Each string should have exactly A 0s, and exactly B 1s in them.

Output Yes if two such different binary strings can be constructed and No otherwise.

Note: 
A string is said to be a palindrome, if the string and the reverse of the string are identical.
Two strings are said to be different if either their lengths are different, or if they differ in at least one character.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case contains two space-separated integers, A and B, in a new line.

------ Output Format ------ 

For each test case, output on a new line 'Yes', if you can construct two different binary strings satisfying the conditions. If not, output No.

You may print each character of the string in uppercase or lowercase (for example, the strings YeS, yes, YES, and YEs will all be treated as identical).

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ A, B ≤ 10^{6}$

----- Sample Input 1 ------ 
3
2 2
2 3
3 3

----- Sample Output 1 ------ 
Yes
Yes
No

----- explanation 1 ------ 
Test case $1$: Consider the binary strings $0110$ and $1001$. Both of them are palindromes, and both of them have exactly $2$ $0$s, and $2$ $1$s. Hence we can construct them, and so the answer is Yes.

Test case $2$: Consider the binary strings $01110$ and $10101$. Both of them are palindromes, and both of them have exactly $2$ $0$s, and $3$ $1$s. Hence we can construct them, and so the answer is Yes.

Test case $3$: There is no way to construct two such different strings. Hence the answer is No.
"""

def can_construct_palindromic_binary_strings(A: int, B: int) -> str:
    # Check if either A or B is less than 2
    if A < 2 or B < 2:
        return 'No'
    
    # Check if both A and B are odd
    if A % 2 == 1 and B % 2 == 1:
        return 'No'
    
    # If none of the above conditions are met, it is possible to construct the strings
    return 'Yes'
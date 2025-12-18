"""
QUESTION:
For encoding an even-length binary string into a sequence of A, T, C, and G, we iterate from left to right and replace the characters as follows:
00 is replaced with A
01 is replaced with T
10 is replaced with C
11 is replaced with G

Given a binary string S of length N (N is even), find the encoded sequence.

------ Input Format ------ 

- First line will contain T, number of test cases. Then the test cases follow.
- Each test case contains two lines of input.
- First line contains a single integer N, the length of the sequence.
- Second line contains binary string S of length N.

------ Output Format ------ 

For each test case, output in a single line the encoded sequence.

Note: Output is case-sensitive.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$2 ≤ N ≤ 10^{3}$
$N$ is even.
- Sum of $N$ over all test cases is at most $10^{3}$.
$S$ contains only characters 0 and 1.

----- Sample Input 1 ------ 
4
2
00
4
0011
6
101010
4
1001

----- Sample Output 1 ------ 
A
AG
CCC
CT
----- explanation 1 ------ 
Test case $1$: Based on the rules 00 is replaced with A.

Test case $2$: Based on the rules 00 is replaced with A. Similarly, 11 is replaced with G. Thus, the encoded sequence is AG.

Test case $3$: The first two characters are 10 which is encoded as C. Similarly, the next two characters 10 are encoded as C and the last two characters 10 are encoded as C. Thus, the encoded string is CCC.

Test case $4$: The first two characters are 10 which is encoded as C. Similarly, the next two characters 01 are encoded as T. Thus, the encoded string is CT.
"""

def encode_binary_string(binary_string: str, length: int = None) -> str:
    """
    Encodes a binary string into a sequence of A, T, C, and G based on the given rules.

    Parameters:
    - binary_string (str): The binary string to be encoded.
    - length (int, optional): The length of the binary string. If not provided, it is inferred from the string length.

    Returns:
    - encoded_string (str): The encoded sequence of A, T, C, and G.
    """
    if length is None:
        length = len(binary_string)
    
    encoded_string = ''
    for k in range(0, length - 1, 2):
        pair = binary_string[k] + binary_string[k + 1]
        if pair == '00':
            encoded_string += 'A'
        elif pair == '01':
            encoded_string += 'T'
        elif pair == '10':
            encoded_string += 'C'
        elif pair == '11':
            encoded_string += 'G'
    
    return encoded_string
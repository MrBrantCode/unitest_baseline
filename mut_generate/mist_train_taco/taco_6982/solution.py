"""
QUESTION:
You are given non-negative integers A, B and C.

Does there exist a non-negative integer X such that A \oplus X+ B \oplus X = C \oplus X?

As a reminder, \oplus denotes the [bitwise XOR operation].

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- The only line of each test case contains three space-separated non-negative integers A, B and C.

------ Output Format ------ 

For each test case, print on a new line the answer: YES if valid X exists, and NO otherwise.

Each character of the output may be printed in either uppercase or lowercase, i.e, the strings Yes, YES, yes, yEs will all be treated as identical.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$0 ≤ A, B, C < 2^{27}$

----- Sample Input 1 ------ 
5
2 5 7
2 3 13
7 0 7
2 7 6
1 6 6

----- Sample Output 1 ------ 
YES
NO
YES
YES
YES

----- explanation 1 ------ 
Test case $1$: $X=0$ satisfies the equation.

Test case $2$: It can be proved that there does not exist a non-negative integer $X$ which satisfies the equation.

Test case $3$: $X=0$ satisfies the equation.

Test case $4$: $X=3$ satisfies the equation.

Test case $5$: $X=1$ satisfies the equation.
"""

def check_valid_x(A: int, B: int, C: int) -> str:
    # Convert A, B, C to their binary representations and strip the '0b' prefix
    a_bin = bin(A)[2:]
    b_bin = bin(B)[2:]
    c_bin = bin(C)[2:]
    
    # Determine the maximum length of the binary strings
    max_len = max(len(a_bin), len(b_bin), len(c_bin))
    
    # Pad the binary strings with leading zeros to make them of equal length
    a_bin = a_bin.zfill(max_len)
    b_bin = b_bin.zfill(max_len)
    c_bin = c_bin.zfill(max_len)
    
    # Initialize a flag to count the number of mismatched bits
    mismatch_count = 0
    
    # Iterate over each bit position
    for i in range(max_len):
        # Check if the current bit combination is a mismatch
        if a_bin[i] + b_bin[i] + c_bin[i] in ('001', '110'):
            mismatch_count += 1
    
    # If the number of mismatches is odd, no valid X exists
    if mismatch_count % 2 == 1:
        return "NO"
    else:
        return "YES"
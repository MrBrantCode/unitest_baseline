"""
QUESTION:
Panda had recently learnt about Bit manipulation and logic gates,now he is very excited about it.One day he came across a very interesting question: Given two numbers,xor them and then in resulting number find the number of set bits.If number of set bits are even then print "YES" otherwise "NO".As he is unable to solve it,he is asking you for help.

Input:
First line of input contains T the number of test cases,then next T lines contains two space separated integers A and B.

Output: 
for each testcase print "YES" if number of set bits are even otherwise "NO" in new line.

Constraints:
1 ≤ T ≤ 500
1 ≤ A,B ≤ 10^9  

SAMPLE INPUT
2
6 5
10 11

SAMPLE OUTPUT
YES
NO
"""

def check_even_set_bits(A: int, B: int) -> str:
    # XOR the two numbers
    x = A ^ B
    
    # Convert the result to binary and count the number of '1's
    set_bits_count = bin(x).count('1')
    
    # Check if the count of set bits is even
    if set_bits_count % 2 == 0:
        return "YES"
    else:
        return "NO"
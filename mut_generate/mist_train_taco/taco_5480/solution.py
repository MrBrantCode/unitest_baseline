"""
QUESTION:
Input

The first line of the input contains a single integer N (1 ≤ N ≤ 24). The next N lines contain 5 space-separated integers each. The first three integers will be between 0 and 2, inclusive. The last two integers will be between 0 and 3, inclusive. The sum of the first three integers will be equal to the sum of the last two integers.

Output

Output the result – a string of lowercase English letters.

Examples

Input


1
1 0 0 1 0


Output


a


Input


10
2 0 0 1 1
1 1 1 2 1
2 1 0 1 2
1 1 0 1 1
2 1 0 2 1
1 1 1 2 1
1 2 1 3 1
2 0 0 1 1
1 1 0 1 1
1 1 2 2 2


Output


codeforcez
"""

def decode_message(N, input_lines):
    A = [
        'a 1 0 0 1 0', 'b 1 1 0 2 0', 'c 2 0 0 1 1', 'd 2 1 0 1 2', 'e 1 1 0 1 1', 
        'f 2 1 0 2 1', 'g 2 2 0 2 2', 'h 1 2 0 2 1', 'i 1 1 0 1 1', 'j 1 2 0 1 2', 
        'k 1 0 1 2 0', 'l 1 1 1 3 0', 'm 2 0 1 2 1', 'n 2 1 1 2 2', 'o 1 1 1 2 1', 
        'p 2 1 1 3 1', 'q 2 2 1 3 2', 'r 1 2 1 3 1', 's 1 1 1 2 1', 't 1 2 1 2 2', 
        'u 1 0 2 2 1', 'v 1 1 2 3 1', 'w 1 2 1 1 3', 'x 2 0 2 2 2', 'y 2 1 2 2 3', 
        'z 1 1 2 2 2'
    ]
    
    decoded_message = []
    
    for line in input_lines:
        for entry in A:
            if entry[2:] == line:
                decoded_message.append(entry[0])
                break
    
    return ''.join(decoded_message)
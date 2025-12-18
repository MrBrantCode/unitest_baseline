"""
QUESTION:
A beautiful sequence is a strictly increasing sequence, in which the term A_{i} divides all A_{j}, where j>i. Given N find a beautiful sequence whose last term is N and the length of the sequence is the maximum possible. If there are multiple solutions return any.
 
Example 1:
Input: N = 10
Output: 1 5 10
Explanation: 10 is divisible by
1 and 5, 5 is divisible by 1.
Example 2:
Input: N = 3
Output: 1 3
Explanation: 3 is divisible by 1.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function FindSequenece() which takes N as an input parameter and returns a list of beautiful sequences. The driver will print two space-separated integers the length of the sequence and an integer x where x = 1 if your sequence is beautiful otherwise x = 0.
 
Expected Time Complexity: O(sqrt(N))
Expected Space Complexity: O(sqrt(N))
 
Constraints:
1 < N < 10^{9}
"""

import math

def generate_beautiful_sequence(N):
    m = int(math.sqrt(N))
    sequence = []
    
    # Find the divisors of N
    for i in range(2, m + 1):
        while N % i == 0:
            sequence.append(N)
            N //= i
    
    # If N is still greater than 1, it must be a prime factor
    if N > 1:
        sequence.append(N)
    
    # Append 1 to the sequence as it is always a part of the beautiful sequence
    sequence.append(1)
    
    # Reverse the sequence to make it strictly increasing
    sequence = sequence[::-1]
    
    return sequence
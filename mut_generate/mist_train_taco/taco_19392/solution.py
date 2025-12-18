"""
QUESTION:
Juggler Sequence is a series of integers in which the first term starts with a positive integer number a and the remaining terms are generated from the immediate previous term using the below recurrence relation:
Given a number N, find the Juggler Sequence for this number as the first term of the sequence.
Example 1:
Input: N = 9
Output: 9 27 140 11 36 6 2 1
Explaination: We start with 9 and use 
above formula to get next terms.
 
Example 2:
Input: N = 6
Output: 6 2 1
Explaination: 
6^{1/2} = 2. 
2^{1/2} = 1.
 
Your Task:
You do not need to read input or print anything. Your Task is to complete the function jugglerSequence() which takes N as the input parameter and returns a list of integers denoting the generated sequence.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1 ≤ N ≤ 100
"""

import math

def generate_juggler_sequence(N):
    if N == 1:
        return [1]
    seq = [N]
    if N % 2 == 0:
        seq.extend(generate_juggler_sequence(int(N ** 0.5)))
    else:
        seq.extend(generate_juggler_sequence(int(N ** 1.5)))
    return seq
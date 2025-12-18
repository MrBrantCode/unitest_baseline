"""
QUESTION:
Kevin has a sequence of integers a1, a2, ..., an. Define the strength of the sequence to be

|a1 - a2| + |a2 - a3| + ... + |an-1 - an| + |an - a1|.

Kevin wants to make his sequence stronger, so he reorders his sequence into a new sequence b1, b2, ..., bn. He wants this new sequence to be as strong as possible. What is the largest possible strength of the resulting sequence?

Input
The input consists of 2 lines. The first line has a positive integer n. The second line contains the n integers a1, a2, ..., an.

Output
Output a single integer: the maximum possible strength.

Constraints
1 ≤ n ≤ 10^5.

|ai| ≤ 10^9. Note that ai can be negative.

SAMPLE INPUT
4
1 2 4 8

SAMPLE OUTPUT
18

Explanation

In the sample case, the original sequence is 1, 2, 4, 8. It's strength is |1-2| + |2-4| + |4-8| + |8-1| = 14.
If Kevin reorders it as 1, 8, 2, 4, the new strength is |1-8| + |8-2| + |2-4| + |4-1| = 18. This is the greatest possible.
"""

def calculate_max_strength(n, sequence):
    # Sort the sequence
    sequence.sort()
    
    # Create a new sequence by interleaving the smallest and largest elements
    m = []
    for j in range(n // 2):
        m.append(sequence[j])
        m.append(sequence[n - j - 1])
    
    # If the sequence length is odd, append the middle element
    if n % 2 != 0:
        m.append(sequence[n // 2])
    
    # Calculate the strength of the new sequence
    s = 0
    for h in range(n - 1):
        s += abs(m[h] - m[h + 1])
    s += abs(m[n - 1] - m[0])
    
    return s
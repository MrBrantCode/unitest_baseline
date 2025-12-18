"""
QUESTION:
A sequence of integers is called a wonderful sequence if all the integers in it are positive and it is a strictly increasing sequence.

Given a sequence of integers, you have to make it a wonderful sequence. For that you can change any element you want, but you should make as less changes as possible in order to make it a wonderful sequence.

Input

The first line of input is an integer T(T ≤ 5), the number of test cases. Each test case contains 2 lines.

The first line of the test case contains an integer (0 < N ≤ 100000), i.e. the number of elements in the original sequence.

The second line contains N positive integers, no larger than 2000000000, which forms the original sequence.

Output

For each test case output the minimal number of elements you must change in the original sequence to make it a wonderful sequence.

SAMPLE INPUT
3
2
1 2
3
3 2 1
5
10 5 6 7 8

SAMPLE OUTPUT
0
2
1

Explanation

For the 1st test case you needn't to change any elements.
For the 2nd test case you can change 3 into 1 and change 1 into 3.
For the 3rd test case you can change 10 into 1.
"""

def make_wonderful_sequence(sequence):
    n = len(sequence)
    if n == 0:
        return 0
    
    count = 0
    
    # Ensure the first element is positive and less than the second element
    if sequence[0] <= 0:
        sequence[0] = 1
        count += 1
    elif n > 1 and sequence[0] >= sequence[1]:
        sequence[0] = sequence[1] - 1
        count += 1
    
    # Iterate through the sequence to ensure it is strictly increasing
    for i in range(1, n):
        if sequence[i] <= sequence[i - 1]:
            sequence[i] = sequence[i - 1] + 1
            count += 1
    
    return count
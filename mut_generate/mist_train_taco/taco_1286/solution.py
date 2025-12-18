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

def min_changes_to_wonderful_sequence(sequence):
    def subsequence(seq):
        if not seq:
            return seq

        M = [None] * len(seq)    # offset by 1 (j -> j-1)
        P = [None] * len(seq)

        L = 1
        M[0] = 0

        for i in range(1, len(seq)):
            lower = 0
            upper = L

            if seq[M[upper-1]] < seq[i]:
                j = upper
            else:
                while upper - lower > 1:
                    mid = (upper + lower) // 2
                    if seq[M[mid-1]] < seq[i]:
                        lower = mid
                    else:
                        upper = mid

                j = lower

            P[i] = M[j-1]

            if j == L or seq[i] < seq[M[j]]:
                M[j] = i
                L = max(L, j+1)

        result = []
        pos = M[L-1]
        for _ in range(L):
            result.append(seq[pos])
            pos = P[pos]

        return result[::-1]

    # Calculate the minimal number of changes
    n = len(sequence)
    b = subsequence(sequence)
    return n - len(b)
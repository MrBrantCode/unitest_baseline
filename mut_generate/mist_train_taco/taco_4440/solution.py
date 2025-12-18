"""
QUESTION:
You are given a sequence of positive integers a_1, a_2, ..., a_{n}. 

While possible, you perform the following operation: find a pair of equal consecutive elements. If there are more than one such pair, find the leftmost (with the smallest indices of elements). If the two integers are equal to x, delete both and insert a single integer x + 1 on their place. This way the number of elements in the sequence is decreased by 1 on each step. 

You stop performing the operation when there is no pair of equal consecutive elements.

For example, if the initial sequence is [5, 2, 1, 1, 2, 2], then after the first operation you get [5, 2, 2, 2, 2], after the second — [5, 3, 2, 2], after the third — [5, 3, 3], and finally after the fourth you get [5, 4]. After that there are no equal consecutive elements left in the sequence, so you stop the process.

Determine the final sequence after you stop performing the operation.


-----Input-----

The first line contains a single integer n (2 ≤ n ≤ 2·10^5) — the number of elements in the sequence.

The second line contains the sequence of integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 10^9).


-----Output-----

In the first line print a single integer k — the number of elements in the sequence after you stop performing the operation. 

In the second line print k integers — the sequence after you stop performing the operation.


-----Examples-----
Input
6
5 2 1 1 2 2

Output
2
5 4 
Input
4
1000000000 1000000000 1000000000 1000000000

Output
1
1000000002 
Input
7
4 10 22 11 12 5 6

Output
7
4 10 22 11 12 5 6 


-----Note-----

The first example is described in the statements.

In the second example the initial sequence is [1000000000, 1000000000, 1000000000, 1000000000]. After the first operation the sequence is equal to [1000000001, 1000000000, 1000000000]. After the second operation the sequence is [1000000001, 1000000001]. After the third operation the sequence is [1000000002].

In the third example there are no two equal consecutive elements initially, so the sequence does not change.
"""

def reduce_sequence(sequence):
    i = 0
    b = []
    n = len(sequence)
    
    while i + 1 < n:
        if sequence[i] == sequence[i + 1]:
            sequence[i + 1] = sequence[i] + 1
            if len(b) > 0:
                sequence[i] = b.pop()
            else:
                i += 1
        else:
            b.append(sequence[i])
            i += 1
    
    b.append(sequence[-1])
    final_length = len(b)
    final_sequence = b
    
    return final_length, final_sequence
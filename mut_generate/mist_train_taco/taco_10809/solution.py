"""
QUESTION:
Snuke got a present from his mother on his birthday. The present was a pair of two sequences a and b, consisting of positive integers. They satisfied all of the following properties:

* The sum of all elements of a is N.
* The sum of all elements of b is N.
* Any string of length N that satisfies the following two conditions (1) and (2) will also satisfy the condition (3).
* (1) Any of the following forms a palindrome: the first a_1 letters, the following a_2 letters, the following a_3 letters and so on.
* (2) Any of the following forms a palindrome: the first b_1 letters, the following b_2 letters, the following b_3 letters and so on.
* (3) All N letters are the same.



He was happy, until one day he lost both of the sequences. Now, he only remembers that the sequence a was a permutation of another sequence A of length M.

To bring him happiness again, his mother has decided to give him another pair of sequences a and b that satisfies his favorite properties and is consistent with his memory.

Constraints

* 1≦N≦10^5
* 1≦M≦100
* 1≦A_i≦10^5
* The sum of all A_i equals N.

Input

The input is given from Standard Input in the following format:


N M
A_1 A_2 ... A_M


Output

If there exists a pair of sequences a and b that satisfies the properties and is consistent with Snuke's memory, print three lines. The first line must contain the sequence a, the second line must contain the length of the sequence b, and the third line must contain the sequence b.

If such a pair does not exist (because Snuke's memory is wrong or some other reason), print a single line containing the word `Impossible` (case-sensitive).

Examples

Input

3 2
2 1


Output

1 2
1
3


Input

6 1
6


Output

6
3
1 2 3


Input

55 10
1 2 3 4 5 6 7 8 9 10


Output

Impossible
"""

def find_happy_sequences(N, M, A):
    # Check if the sum of A equals N
    if sum(A) != N:
        return 'Impossible'
    
    # Sort A in descending order
    A.sort(reverse=True)
    
    # Check for the condition that ensures a valid sequence a
    for i in range(1, M - 1):
        if A[i] % 2 == 1:
            if A[0] % 2 == 1:
                if A[-1] % 2 == 1:
                    return 'Impossible'
                else:
                    A[i], A[-1] = A[-1], A[i]
            else:
                A[i], A[0] = A[0], A[i]
    
    # Construct sequence a
    a = A[:]
    
    # Construct sequence b
    if M == 1:
        if a[0] > 1:
            a[0] -= 1
            a.append(1)
            b_length = M + 1
        else:
            b_length = M
    elif a[-1] == 1:
        b_length = M - 1
        a.pop()
        a[0] += 1
    else:
        b_length = M
        a[0] += 1
        a[-1] -= 1
    
    # Construct sequence b based on the modified a
    b = [1] * b_length
    
    return a, b_length, b
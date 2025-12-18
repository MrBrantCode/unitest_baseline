"""
QUESTION:
There are N arrays. The length of each array is M and initially each array contains integers (1，2，...，M) in this order.

Mr. Takahashi has decided to perform Q operations on those N arrays. For the i-th (1≤i≤Q) time, he performs the following operation.

* Choose an arbitrary array from the N arrays and move the integer a_i (1≤a_i≤M) to the front of that array. For example, after performing the operation on a_i=2 and the array (5，4，3，2，1), this array becomes (2，5，4，3，1).



Mr. Takahashi wants to make N arrays exactly the same after performing the Q operations. Determine if it is possible or not.

Constraints

* 2≤N≤10^5
* 2≤M≤10^5
* 1≤Q≤10^5
* 1≤a_i≤M

Input

The input is given from Standard Input in the following format:


N M
Q
a_1 a_2 ... a_Q


Output

Print `Yes` if it is possible to make N arrays exactly the same after performing the Q operations. Otherwise, print `No`.

Examples

Input

2 2
3
2 1 2


Output

Yes


Input

3 2
3
2 1 2


Output

No


Input

2 3
3
3 2 1


Output

Yes


Input

3 3
6
1 2 2 3 3 3


Output

No
"""

def can_make_arrays_identical(N, M, Q, operations):
    def reads(offset=0):
        return [int(i) - offset for i in operations.split(' ')]

    def Judge(vector):
        length = len(vector) - 1
        for i in range(length):
            if vector[i] > vector[i + 1]:
                return 0
        return 1

    A = reads(1)
    pos = [-1] * M
    pat = []
    freq = [0] * (M + 1)
    freq[0] = N
    found = set()
    counter = 0

    for i in A[::-1]:
        if i not in found:
            pat.append(i)
            found.add(i)
            pos[i] = counter
            counter += 1
            if counter == M:
                break

    for i in range(M):
        if pos[i] == -1:
            pat.append(i)

    for i in A[::-1]:
        temp = pos[i]
        if freq[temp] > 0:
            freq[temp] -= 1
            freq[temp + 1] += 1

    start = M
    for i in range(M):
        if freq[i] != 0:
            start = i
            break

    return "Yes" if Judge(pat[start:]) else "No"
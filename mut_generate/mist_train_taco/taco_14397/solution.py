"""
QUESTION:
prison

There are an infinite number of prisoners. Initially, the prisoners are numbered 0, 1, 2, ....

Do the following N times:

* Release the 0th prisoner and execute the k, 2k, 3k, ... th prisoners.
* Then renumber the remaining prisoners. At this time, the prisoners with the smallest original numbers are numbered 0, 1, 2, ... in order.



Find the number that was originally assigned to the prisoner released in the Nth operation.

Constraints

* 1 ≤ N ≤ 10 ^ 5
* 2 ≤ k ≤ 10 ^ 5
* The answer is less than 10 ^ {18}.



Input Format

Input is given from standard input in the following format.


N k


Output Format

Print the answer in one line.

Sample Input 1


4 2


Sample Output 1


7


Sample Input 2


13


Sample Output 2


0


Sample Input 3


100000 100000


Sample Output 3


99999






Example

Input

4 2


Output

7
"""

def find_nth_released_prisoner(N, k):
    a = 0
    for i in range(N - 1):
        a = a * k // (k - 1) + 1
    return a
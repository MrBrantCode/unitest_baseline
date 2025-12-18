"""
QUESTION:
Snuke has an integer sequence A of length N.

He will freely choose an integer b. Here, he will get sad if A_i and b+i are far from each other. More specifically, the sadness of Snuke is calculated as follows:

* abs(A_1 - (b+1)) + abs(A_2 - (b+2)) + ... + abs(A_N - (b+N))



Here, abs(x) is a function that returns the absolute value of x.

Find the minimum possible sadness of Snuke.

Constraints

* 1 \leq N \leq 2 \times 10^5
* 1 \leq A_i \leq 10^9
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
A_1 A_2 ... A_N


Output

Print the minimum possible sadness of Snuke.

Examples

Input

5
2 2 3 5 5


Output

2


Input

9
1 2 3 4 5 6 7 8 9


Output

0


Input

6
6 5 4 3 2 1


Output

18


Input

7
1 1 1 1 2 3 4


Output

6
"""

def calculate_minimum_sadness(N, A):
    # Adjust the sequence elements as per the problem statement
    for i in range(N):
        A[i] -= i + 1
    
    # Sort the adjusted sequence
    A.sort()
    
    # Find the median of the adjusted sequence
    m = A[N // 2]
    
    # Calculate the minimum sadness
    sum = 0
    for x in A:
        sum += abs(x - m)
    
    return sum
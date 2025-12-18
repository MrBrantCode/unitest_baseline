"""
QUESTION:
Statement: Write a code to display all the non-prime numbers upto N.

Input: Only the value of N.

Output: The numbers which are not prime upto N (including N), each in a new line.

Constraints: 1 ≤ N ≤ 10^4

SAMPLE INPUT
25

SAMPLE OUTPUT
4
6
8
9
10
12
14
15
16
18
20
21
22
24
25

Explanation

In the above case, input is 25 (i.e., N=25) and the corresponding output is given alongside. Output contains only the non prime numbers upto 25.
"""

def find_non_prime_numbers(N):
    non_prime_numbers = []
    
    for i in range(2, N + 1):
        flag = 0
        for j in range(2, int(i / 2) + 1):
            if i % j == 0:
                flag = 1
                break
        if flag == 1:
            non_prime_numbers.append(i)
    
    return non_prime_numbers
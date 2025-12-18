"""
QUESTION:
Today is Sid’s birthday and he is very excited about this as he is giving a special birthday party to all his friends. In this party they are going to play a game for which Sid have to arrange all his friends in a row such that no two boys should be present which are adjacent to each other. There are total M girls and N boys in the party excluding the Sid.

You are his best friend Sonu and he is asking for your help to find the number of ways he can arrange his friends in a row according to the given condition.

If no  such arrangement is possible, print -1.

Input
The first line contains one number T representing the number of test cases.
Each test case contains two integers, M representing the number of girls and N representing the number of boys.

Output
For each test case, you need to find the number of different ways to arrange Sid’s friends. As the answer can be very large you need to print the  answer modulo (1000000007).

Constraints
1 ≤ T ≤ 100000
1 ≤ M ≤ 50
1 ≤ N ≤ 50

SAMPLE INPUT
1
3 2

SAMPLE OUTPUT
72
"""

def calculate_arrangements(M, N):
    MOD = 1000000007
    
    if M < N - 1:
        return -1
    
    res = 1
    for i in range(M + 1 - N + 1, M + 2):
        res = (res * i) % MOD
    for i in range(1, M + 1):
        res = (res * i) % MOD
    
    return res
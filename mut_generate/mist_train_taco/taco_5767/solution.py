"""
QUESTION:
Alice has just learnt multiplying two integers. He wants to multiply two integers X and Y to form a number Z. To make the problem interesting he will choose X in the range [1,M] and Y in the range [1,N]. Help him to find the number of ways in which he can do this.

Input
First line of the input is the number of test cases T. It is followed by T lines. Each line has three space separated integers, the numbers Z, M and N.

Output 
For each test case output a single integer, the number of ways.

Constraints
1 ≤ T ≤ 50 
1 ≤ Z ≤ 10^12
1 ≤ M ≤ 10^12
1 ≤ N ≤ 10^12

SAMPLE INPUT
4
4 7 9
5 2 10
5 5 6
2 8 1

SAMPLE OUTPUT
3
1
2
1
"""

def count_multiplication_ways(Z, M, N):
    l = []
    for i in range(1, int(Z**0.5) + 1):
        if Z % i == 0:
            if i != Z // i:
                l.append(i)
                l.append(Z // i)
            else:
                l.append(i)
    
    if M < N:
        min1 = M
        max1 = N
    else:
        min1 = N
        max1 = M
    
    count = 0
    for i in l:
        if i <= min1:
            if (Z // i) <= max1:
                count += 1
    
    return count
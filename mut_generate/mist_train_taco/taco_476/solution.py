"""
QUESTION:
Everyone has got to know that HELL and Printf{} use cheats while playing Counter-Strike 1.6. Everyone decides to give them a punishment.
They are going to be made to paint all the rooms of the ground floor of the hostel. 

There are a total of N rooms on the ground floor arranged in a single row side by side numbered from 1 to N. HELL has to paint all the rooms with room numbers 1 to K (both inclusive) and Printf{} has to paint all the rooms with room numbers K+1 to N (both inclusive).

Both are given a total of 10 paints of distinct colours, 1 of them being White colour. They have to paint all the rooms such that atleast one of the rooms painted by each one of them is not White in colour so that the hostel ground floor has a minimum of two colourful (non-White) rooms. 

Given N and K, you have to report the total number of different possible appearances of the hostel ground floor ie. , total number of different ways in which all the rooms of the ground floor can be painted. Assume that there is infinite amount of paint of each colour made available to both of them.

Input :

The first line comprises of T denoting the number of test cases. The next T lines are such that each line consists of 2 space separated integers N and K.

Output :

Print a single integer , the answer to each test case on a new line. 

Constraints:

1 ≤ T ≤ 5

2 ≤ N ≤ 100000

1 ≤ K<N

Author : Shreyans

Tester : Sayan

(By IIT Kgp HackerEarth Programming Club)

SAMPLE INPUT
2
2 1
3 2

SAMPLE OUTPUT
81
891
"""

def calculate_total_paintings(N, K):
    # Calculate the total number of ways HELL can paint the first K rooms
    a = pow(10, K)
    
    # Calculate the total number of ways Printf can paint the remaining N-K rooms
    b = pow(10, N - K)
    
    # Calculate the total number of different possible appearances
    # Subtract the cases where all rooms are white for both HELL and Printf
    c = (a * b) - a - b + 1
    
    return c
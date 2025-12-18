"""
QUESTION:
Alice is climbing stairs. There are total N stairs. She climbs A stairs upwards in day and she comes downstairs in night by B stairs. Find number of days she will take to reach the top of staircase.   

Input: 
First and only line contains three space separated integers denoting A, B, N.

Output: 
Print only one line of output denoting the answer to the question.

Constraints: 
1 ≤ B<A≤N ≤ 10^9

SAMPLE INPUT
5 1 6

SAMPLE OUTPUT
2
"""

def calculate_days_to_climb(A: int, B: int, N: int) -> int:
    # Calculate the initial number of days
    X = (N - A) // (A - B) + 1
    
    # Adjust for any remaining stairs after the initial calculation
    if (N - A) % (A - B) > 0:
        X += 1
    
    return X
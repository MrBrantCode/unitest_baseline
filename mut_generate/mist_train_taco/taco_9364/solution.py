"""
QUESTION:
View Russian Translation

The great Kian is looking for a smart prime minister. He's looking for a guy who can solve the OLP (Old Legendary Problem). OLP is an old problem (obviously) that no one was able to solve it yet (like P=NP).

But still, you want to be the prime minister really bad. So here's the problem:

Given the sequence a1, a2, ..., an find the three values a1 + a4 + a7 + ..., a2 + a5 + a8 + ... and a3 + a6 + a9 + ... (these summations go on while the indexes are valid).

Input
The first line of input contains a single integer n (1 ≤ n ≤ 10^5).

The second line contains n integers a1, a2, ..., an separated by space (1 ≤ ai ≤ 10^9).

Output
Print three values in one line (the answers).

SAMPLE INPUT
5
1 2 3 4 5SAMPLE OUTPUT
5 7 3
"""

def calculate_olp_sums(n, arr):
    a = 0
    b = 0
    c = 0
    
    for i in range(0, n, 3):
        if i < n:
            a += arr[i]
        if i + 1 < n:
            b += arr[i + 1]
        if i + 2 < n:
            c += arr[i + 2]
    
    return (a, b, c)
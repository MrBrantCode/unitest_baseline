"""
QUESTION:
On the way to Dandi March, Gandhijee carried a mirror with himself. When he reached Dandi, he decided to play a game with the tired people to give them some strength. At each turn of the game he pointed out a person and told him to say a number N(possibly huge) of his choice. The number was called lucky if that equals it's mirror image.

Input: 
First line contains number of test cases T. Each test case contains a single integer N.

Output: 
For each test case print "YES" if the number was lucky else print "NO" (quotes for clarity) in one line.

Constraints:
1 ≤ T ≤ 100
0 ≤ N ≤ 10^100Image for Sample Test Cases :SAMPLE INPUT
2
101
020

SAMPLE OUTPUT
YES
NO

Explanation

For 1st case, as clear from the image "101" and it's mirror image are identical. Hence, output "YES".
For 2nd case, "020" and it's mirror image are not identical. Hence output "NO".
"""

def is_lucky_number(N: str) -> str:
    # Check if all characters in the number are valid lucky digits (0, 1, 8)
    for char in N:
        if char not in '018':
            return "NO"
    
    # Check if the number is the same as its reverse
    if N == N[::-1]:
        return "YES"
    else:
        return "NO"
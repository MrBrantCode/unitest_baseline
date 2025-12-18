"""
QUESTION:
Find the edit distance between given two words s1 and s2.

The disntace is the minimum number of single-character edits required to change one word into the other. The edits including the following operations:

* insertion: Insert a character at a particular position.
* deletion: Delete a character at a particular position.
* substitution: Change the character at a particular position to a different character

Constraints

* 1 ≤ length of s1 ≤ 1000
* 1 ≤ length of s2 ≤ 1000

Input


s1
s2


Two words s1 and s2 are given in the first line and the second line respectively. The words will consist of lower case characters.

Output

Print the edit distance in a line.

Examples

Input

acac
acm


Output

2


Input

icpc
icpc


Output

0
"""

def calculate_edit_distance(s1: str, s2: str) -> int:
    # Initialize the distance matrix
    dist = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
    
    # Fill the first row and first column of the matrix
    for i in range(len(s1) + 1):
        dist[0][i] = i
    for i in range(len(s2) + 1):
        dist[i][0] = i
    
    # Fill the rest of the matrix
    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            k = 1
            if s1[j - 1] == s2[i - 1]:
                k = 0
            dist[i][j] = min(dist[i - 1][j] + 1, dist[i][j - 1] + 1, dist[i - 1][j - 1] + k)
    
    # The edit distance is the value in the bottom-right corner of the matrix
    return dist[len(s2)][len(s1)]
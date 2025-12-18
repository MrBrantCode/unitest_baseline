"""
QUESTION:
Given is a string S consisting of digits from 1 through 9.
Find the number of pairs of integers (i,j) (1 ≤ i ≤ j ≤ |S|) that satisfy the following condition:
Condition: In base ten, the i-th through j-th characters of S form an integer that is a multiple of 2019.

-----Constraints-----
 - 1 ≤ |S| ≤ 200000
 - S is a string consisting of digits from 1 through 9.

-----Input-----
Input is given from Standard Input in the following format:
S

-----Output-----
Print the number of pairs of integers (i,j) (1 ≤ i ≤ j ≤ |S|) that satisfy the condition.

-----Sample Input-----
1817181712114

-----Sample Output-----
3

Three pairs - (1,5), (5,9), and (9,13) - satisfy the condition.
"""

def count_multiples_of_2019(S: str) -> int:
    p = 2019
    S = S[::-1]  # Reverse the string to process from the least significant digit
    d = 0
    z = [0] * p
    
    for i, char in enumerate(S):
        d = (d + int(char) * pow(10, i, p)) % p
        z[d] += 1
    
    r = z[0]
    for count in z:
        if count > 1:
            r += count * (count - 1) // 2
    
    return r
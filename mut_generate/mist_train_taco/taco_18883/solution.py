"""
QUESTION:
Given is a string S. Let T be the concatenation of K copies of S. We can repeatedly perform the following operation: choose a character in T and replace it with a different character. Find the minimum number of operations required to satisfy the following condition: any two adjacent characters in T are different.

Constraints

* 1 \leq |S| \leq 100
* S consists of lowercase English letters.
* 1 \leq K \leq 10^9
* K is an integer.

Input

Input is given from Standard Input in the following format:


S
K


Output

Print the minimum number of operations required.

Examples

Input

issii
2


Output

4


Input

qq
81


Output

81


Input

cooooooooonteeeeeeeeeest
999993333


Output

8999939997
"""

def min_operations_to_diff_adjacent_chars(S: str, K: int) -> int:
    # If all characters in S are the same, the problem simplifies
    if len(set(S)) == 1:
        return len(S) * K // 2
    
    # Count the number of operations needed within one copy of S
    m = 0
    j = 0
    while j < len(S) - 1:
        if S[j] == S[j + 1]:
            m += 1
            j += 1  # Skip the next character as it's part of the same sequence
        j += 1
    
    # Total operations for K copies of S
    total_operations = m * K
    
    # Check if the first and last characters of S are the same
    if S[0] == S[-1]:
        # Adjust for the overlap between the last character of one copy and the first of the next
        total_operations += K - 1
    
    return total_operations
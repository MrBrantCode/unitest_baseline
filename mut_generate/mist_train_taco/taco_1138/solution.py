"""
QUESTION:
Given an integer n. Print first n elements of Recaman’s sequence.
It is basically a function with domain and co-domain as natural numbers and 0. It is recursively defined as below:
Specifically, let a(n) denote the (n+1)-th term. (0 being already there).
The rule says:
a(0) = 0
a(n) = a(n-1) - n      if a(n-1) - n > 0 and is not already present in the sequence
       =  a(n-1) + n    otherwise. 
Example 1:
Input: n = 6
Output: 0 1 3 6 2 7
Explaination: Follow the rule and this 
will be the output.
Example 2:
Input: n = 3
Output: 0 1 3
Explaination: If the rule is followed, 
it will produce this output.
Your Task:
You do not need to read input or print anything. Your task is to complete the function recamanSequence() which takes n as the input parameter and returns the sequence.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)
Constraints:
1 ≤ n ≤ 100
"""

def generate_recaman_sequence(n: int) -> list[int]:
    if n <= 0:
        return []
    
    sequence = [0] * n
    
    for i in range(1, n):
        minus_val = sequence[i - 1] - i
        if minus_val > 0 and minus_val not in sequence:
            sequence[i] = minus_val
        else:
            sequence[i] = sequence[i - 1] + i
    
    return sequence
"""
QUESTION:
Write a program which reads an integer n and identifies the number of combinations of a, b, c and d (0 ≤ a, b, c, d ≤ 9) which meet the following equality:

a + b + c + d = n

For example, for n = 35, we have 4 different combinations of (a, b, c, d): (8, 9, 9, 9), (9, 8, 9, 9), (9, 9, 8, 9), and (9, 9, 9, 8).



Input

The input consists of several datasets. Each dataset consists of n (1 ≤ n ≤ 50) in a line. The number of datasets is less than or equal to 50.

Output

Print the number of combination in a line.

Example

Input

35
1


Output

4
4
"""

def count_combinations(n: int) -> int:
    # Initialize a list to store the number of combinations for each possible sum
    answer = [0] * 51
    
    # Iterate over all possible values of a, b, c, and d
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    # Calculate the sum of a, b, c, and d
                    current_sum = a + b + c + d
                    # Increment the count for this sum
                    answer[current_sum] += 1
    
    # Return the number of combinations for the given n
    return answer[n]
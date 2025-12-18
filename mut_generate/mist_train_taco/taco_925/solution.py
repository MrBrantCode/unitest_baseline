"""
QUESTION:
You are given positive integers A and B.
Find the K-th largest positive integer that divides both A and B.
The input guarantees that there exists such a number.

-----Constraints-----
 - All values in input are integers.
 - 1 \leq A, B \leq 100
 - The K-th largest positive integer that divides both A and B exists.
 - K \geq 1

-----Input-----
Input is given from Standard Input in the following format:
A B K

-----Output-----
Print the K-th largest positive integer that divides both A and B.

-----Sample Input-----
8 12 2

-----Sample Output-----
2

Three positive integers divides both 8 and 12: 1, 2 and 4.
Among them, the second largest is 2.
"""

def find_kth_largest_divisor(A: int, B: int, K: int) -> int:
    # Initialize an empty list to store common divisors
    divisors = []
    
    # Iterate from 1 to the minimum of A and B
    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            divisors.append(i)
    
    # Return the K-th largest divisor (which is the K-th element from the end)
    return divisors[-K]
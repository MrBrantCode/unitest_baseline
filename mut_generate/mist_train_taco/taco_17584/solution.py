"""
QUESTION:
As the Rohan is also taking part in the CodeWealth Series, this week he learned about hashing. Now he wants to practice some problems. So he came up with a simple problem. Firstly, he made a hash function F such that:

F(x) = x % 10

Now using this function he wants to hash N integers and count the number of collisions that will occur while hashing the integers.

Input:

The first line contains an integer T, denoting the number of test cases.

The first line of each test case contains an integer N, denoting the number of integers to hash.

The next line contains N space separated integers, denoting the integer X to hash.

Output:

For each test case, print the number of collisions that will occur while hashing the integers.

Constraints:

1 ≤ T ≤ 10

1 ≤ N ≤ 100

0 ≤ X ≤ 105

SAMPLE INPUT
2
3
1 2 3
4
1 1 2 3

SAMPLE OUTPUT
0
1

Explanation

In the first case, there will be no collisions as each integer will be hashed to a different index.

F(1) = 1 % 10 = 1

F(2) = 2 % 10 = 2

F(3) = 3 % 10 = 3

In the second case, there will be 1 collision at index 1 as the first two integers will hash to the same index.
"""

def count_hash_collisions(test_cases):
    results = []
    
    for case in test_cases:
        n = len(case)
        hash_counts = [0] * 10
        
        for num in case:
            hash_index = num % 10
            hash_counts[hash_index] += 1
        
        collisions = 0
        for count in hash_counts:
            if count > 1:
                collisions += (count - 1)
        
        results.append(collisions)
    
    return results
"""
QUESTION:
Snuke has N dogs and M monkeys. He wants them to line up in a row.
As a Japanese saying goes, these dogs and monkeys are on bad terms. ("ken'en no naka", literally "the relationship of dogs and monkeys", means a relationship of mutual hatred.) Snuke is trying to reconsile them, by arranging the animals so that there are neither two adjacent dogs nor two adjacent monkeys.
How many such arrangements there are? Find the count modulo 10^9+7 (since animals cannot understand numbers larger than that).
Here, dogs and monkeys are both distinguishable. Also, two arrangements that result from reversing each other are distinguished.

-----Constraints-----
 - 1 ≤ N,M ≤ 10^5

-----Input-----
Input is given from Standard Input in the following format:
N M

-----Output-----
Print the number of possible arrangements, modulo 10^9+7.

-----Sample Input-----
2 2

-----Sample Output-----
8

We will denote the dogs by A and B, and the monkeys by C and D. There are eight possible arrangements: ACBD, ADBC, BCAD, BDAC, CADB, CBDA, DACB and DBCA.
"""

import math

def count_valid_arrangements(n: int, m: int) -> int:
    mod = 10 ** 9 + 7
    
    # Check if the difference between the number of dogs and monkeys is more than 1
    if abs(n - m) > 1:
        return 0
    
    # Calculate factorials
    dog_factorial = math.factorial(n)
    monkey_factorial = math.factorial(m)
    
    # Calculate the number of valid arrangements
    if abs(n - m) == 1:
        ans = dog_factorial * monkey_factorial % mod
    elif n == m:
        ans = dog_factorial * monkey_factorial * 2 % mod
    
    return ans
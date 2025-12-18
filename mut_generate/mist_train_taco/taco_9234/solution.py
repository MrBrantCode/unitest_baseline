"""
QUESTION:
Today, teacher taught Xenny the chapter 'Prime numbers and Composite numbers'. Xenny liked it and being a studious boy, wanted some homework. So teacher gave him a simple task. The task is to find the smallest composite number greater than given no. Xenny was happy to get the simple task. But Xenny didn't get the time for complting the homework being busy in helping his mother throughout the day. You, a best friend of Xenny, don't want Xenny to get punished by teacher. So its your job to complete his homework.
Formally, there will be t numbers and you have to find smallest greater composite number for each of them.

Input:

The first line of input will be t i.e. number of test-cases.
Followed by t lines each containing n.

Output:

For each test-case, Print the smallest greater number than n which is a composite number on new line.

Constraints:

SMALL:

1 ≤ t ≤ 10

0 ≤ n ≤ 10

MEDIUM:

1 ≤ t ≤ 500

0 ≤ n ≤ 1000

LARGE:

1 ≤ t ≤ 50000

0 ≤ n ≤ 100000

SAMPLE INPUT
2
3
8

SAMPLE OUTPUT
4
9

Explanation

Test-cases are 2.
For first case, the smallest composite no. greater than 3 is 4 .
For second case, the smallest composite no. greater than 8 is 9 .
"""

def find_smallest_composite_greater_than(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    for i in range(n + 1, n + 1000):  # A larger range to ensure we find a composite number
        if not is_prime(i):
            return i

    return None  # In case no composite number is found within the range (shouldn't happen with given constraints)
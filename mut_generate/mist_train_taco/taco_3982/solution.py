"""
QUESTION:
Sasha likes investigating different math objects, for example, magic squares. But Sasha understands that magic squares have already been studied by hundreds of people, so he sees no sense of studying them further. Instead, he invented his own type of square — a prime square. 

A square of size n × n is called prime if the following three conditions are held simultaneously: 

  * all numbers on the square are non-negative integers not exceeding 10^5; 
  * there are no prime numbers in the square; 
  * sums of integers in each row and each column are prime numbers. 



Sasha has an integer n. He asks you to find any prime square of size n × n. Sasha is absolutely sure such squares exist, so just help him!

Input

The first line contains a single integer t (1 ≤ t ≤ 10) — the number of test cases.

Each of the next t lines contains a single integer n (2 ≤ n ≤ 100) — the required size of a square.

Output

For each test case print n lines, each containing n integers — the prime square you built. If there are multiple answers, print any.

Example

Input


2
4
2


Output


4 6 8 1
4 9 9 9
4 10 10 65
1 4 4 4
1 1
1 1
"""

def generate_prime_square(n):
    """
    Generates a prime square of size n x n.

    A prime square is defined as a square where:
    - All numbers on the square are non-negative integers not exceeding 10^5.
    - There are no prime numbers in the square.
    - Sums of integers in each row and each column are prime numbers.

    Parameters:
    n (int): The size of the square (n x n).

    Returns:
    list of lists: A 2D list representing the prime square.
    """
    square = [[0] * n for _ in range(n)]
    
    for j in range(n):
        b = [0] * n
        b[j] = 1
        b[-j - 1] = 1
        if j != n - 1 and j != n // 2:
            square[j] = b
        elif n % 2 == 0:
            square[j] = b
        else:
            if j == n - 1:
                b[n // 2] = 1
                square[j] = b
            if j == n // 2:
                b[n // 2 - 1] = 1
                square[j] = b
    
    return square
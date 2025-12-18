"""
QUESTION:
Find the minimum prime number greater than or equal to X.

-----Notes-----
A prime number is an integer greater than 1 that cannot be evenly divided by any positive integer except 1 and itself.
For example, 2, 3, and 5 are prime numbers, while 4 and 6 are not.

-----Constraints-----
 -  2 \le X \le 10^5 
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
X

-----Output-----
Print the minimum prime number greater than or equal to X.

-----Sample Input-----
20

-----Sample Output-----
23

The minimum prime number greater than or equal to 20 is 23.
"""

def find_min_prime_greater_equal_to(X: int) -> int:
    """
    Finds the minimum prime number greater than or equal to X.

    Parameters:
    X (int): The starting point to find the minimum prime number.

    Returns:
    int: The minimum prime number greater than or equal to X.
    """
    while True:
        check = True
        for i in range(2, int(X ** 0.5) + 1):
            if X % i == 0:
                X += 1
                check = False
                break
        if check:
            return X
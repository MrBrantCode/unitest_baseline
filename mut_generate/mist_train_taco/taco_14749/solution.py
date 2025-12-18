"""
QUESTION:
Problem Statement:

Tom is collecting money for his birthday party, he is having 'a' coins today and his father gives him 'k' coins each day. 

Since his birthday is on 'nth' day, he wants to know the amount of money he will have on his birthday.

Tom is weak at maths, help him calculate the number of coins he will have on his birthday.

Input:

The first line of input contains an integer 'T' denoting the number of test cases.
Each line of test case contains 3 space seperated integers 'a', 'k', 'n' .

Output:

For each test case, output the number of coins Tom will have on his birthday.

Constraints:

1 ≤ T ≤ 100

1 ≤ a,n ≤ 100

0 ≤ k ≤ 100

SAMPLE INPUT
3
2 2 3
1 2 3
1 0 3

SAMPLE OUTPUT
6
5
1

Explanation

In test case 1, a=2, k=2 and n=3. since today he has 2 coins and his father gives him 2 coins each day, on the 3rd day he will have 2+2+2=6 coins
"""

def calculate_coins_on_birthday(a: int, k: int, n: int) -> int:
    """
    Calculate the number of coins Tom will have on his birthday.

    Parameters:
    a (int): The initial number of coins Tom has today.
    k (int): The number of coins Tom's father gives him each day.
    n (int): The number of days until Tom's birthday.

    Returns:
    int: The total number of coins Tom will have on his birthday.
    """
    for i in range(1, n):
        a += k
    return a
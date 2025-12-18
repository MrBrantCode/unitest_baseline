"""
QUESTION:
Kurohashi has never participated in AtCoder Beginner Contest (ABC).
The next ABC to be held is ABC N (the N-th ABC ever held).
Kurohashi wants to make his debut in some ABC x such that all the digits of x in base ten are the same.
What is the earliest ABC where Kurohashi can make his debut?

-----Constraints-----
 - 100 \leq N \leq 999
 - N is an integer.

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
If the earliest ABC where Kurohashi can make his debut is ABC n, print n.

-----Sample Input-----
111

-----Sample Output-----
111

The next ABC to be held is ABC 111, where Kurohashi can make his debut.
"""

def find_earliest_debut_abc(N: int) -> int:
    """
    Finds the earliest ABC where Kurohashi can make his debut such that all the digits of the ABC number are the same.

    Parameters:
    - N (int): The next ABC to be held (100 ≤ N ≤ 999).

    Returns:
    - int: The earliest ABC number where all digits are the same.
    """
    first_digit = str(N)[0]
    candidate = int(first_digit * 3)
    
    if N <= candidate:
        return candidate
    else:
        return int(str(int(first_digit) + 1) * 3)
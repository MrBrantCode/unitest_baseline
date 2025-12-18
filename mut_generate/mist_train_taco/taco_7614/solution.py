"""
QUESTION:
It is November 18 now in Japan. By the way, 11 and 18 are adjacent Lucas numbers.
You are given an integer N. Find the N-th Lucas number.
Here, the i-th Lucas number L_i is defined as follows:
 - L_0=2
 - L_1=1
 - L_i=L_{i-1}+L_{i-2} (i≥2)

-----Constraints-----
 - 1≤N≤86
 - It is guaranteed that the answer is less than 10^{18}.
 - N is an integer.

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the N-th Lucas number.

-----Sample Input-----
5

-----Sample Output-----
11

 - L_0=2
 - L_1=1
 - L_2=L_0+L_1=3
 - L_3=L_1+L_2=4
 - L_4=L_2+L_3=7
 - L_5=L_3+L_4=11
Thus, the 5-th Lucas number is 11.
"""

def calculate_lucas_number(N: int) -> int:
    """
    Calculate the N-th Lucas number.

    The Lucas numbers are defined as:
    - L_0 = 2
    - L_1 = 1
    - L_i = L_{i-1} + L_{i-2} for i >= 2

    Parameters:
    N (int): The position of the Lucas number to be calculated.

    Returns:
    int: The N-th Lucas number.
    """
    if N == 0:
        return 2
    elif N == 1:
        return 1
    else:
        n_2 = 2
        n_1 = 1
        for _ in range(N - 1):
            n_0 = n_1 + n_2
            n_2 = n_1
            n_1 = n_0
        return n_0
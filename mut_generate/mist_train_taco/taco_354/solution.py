"""
QUESTION:
Given positive integers N, K and M, solve the following problem for every integer x between 1 and N (inclusive):
 - Find the number, modulo M, of non-empty multisets containing between 0 and K (inclusive) instances of each of the integers 1, 2, 3 \cdots, N such that the average of the elements is x.

-----Constraints-----
 - 1 \leq N, K \leq 100
 - 10^8 \leq M \leq 10^9 + 9
 - M is prime.
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N K M

-----Output-----
Use the following format:
c_1
c_2
:
c_N

Here, c_x should be the number, modulo M, of multisets such that the average of the elements is x.

-----Sample Input-----
3 1 998244353

-----Sample Output-----
1
3
1

Consider non-empty multisets containing between 0 and 1 instance(s) of each of the integers between 1 and 3. Among them, there are:
 - one multiset such that the average of the elements is k = 1: \{1\};
 - three multisets such that the average of the elements is k = 2: \{2\}, \{1, 3\}, \{1, 2, 3\};
 - one multiset such that the average of the elements is k = 3: \{3\}.
"""

def count_multisets_by_average(N: int, K: int, M: int) -> list[int]:
    """
    Calculate the number of non-empty multisets containing between 0 and K instances
    of each of the integers 1 through N such that the average of the elements is x,
    for each x from 1 to N, modulo M.

    Parameters:
    - N (int): The maximum integer value in the multisets.
    - K (int): The maximum number of instances of each integer in the multisets.
    - M (int): The modulus for the result.

    Returns:
    - list[int]: A list of integers where the i-th element represents the number of
                 multisets such that the average of the elements is i+1, modulo M.
    """
    R = range
    T = [[1]]
    
    for i in R(1, N):
        q = K * i
        if i > ~i + N:
            T += [(y := T[-1][:len(T[~i + N])])]
        else:
            T += [(y := (T[-1][:] + [0] * q))]
        p = len(y) - i
        for j in R(p):
            y[j + i] += y[j] % M
        for j in R(p - q):
            y[~j] -= y[~j - i - q] % M
    
    result = []
    for i in R(N):
        result.append(sum((T[i][j] * T[~i + N][j] for j in R(len(T[i])))) * -~K % M - 1)
    
    return result
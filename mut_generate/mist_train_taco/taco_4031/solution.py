"""
QUESTION:
Print all the integers that satisfies the following in ascending order:
 - Among the integers between A and B (inclusive), it is either within the K smallest integers or within the K largest integers.

-----Constraints-----
 - 1 \leq A \leq B \leq 10^9
 - 1 \leq K \leq 100
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
A B K

-----Output-----
Print all the integers that satisfies the condition above in ascending order.

-----Sample Input-----
3 8 2

-----Sample Output-----
3
4
7
8

 - 3 is the first smallest integer among the integers between 3 and 8.
 - 4 is the second smallest integer among the integers between 3 and 8.
 - 7 is the second largest integer among the integers between 3 and 8.
 - 8 is the first largest integer among the integers between 3 and 8.
"""

def find_special_integers(A: int, B: int, K: int) -> list[int]:
    """
    Find and return all integers between A and B (inclusive) that are either within the K smallest or K largest integers.

    Parameters:
    - A (int): The lower bound of the range (inclusive).
    - B (int): The upper bound of the range (inclusive).
    - K (int): The number of smallest and largest integers to consider.

    Returns:
    - list[int]: A list of integers that satisfy the condition, sorted in ascending order.
    """
    ans = []
    for i in range(K):
        if A <= A + i <= B:
            ans.append(A + i)
        if A <= B - i <= B:
            ans.append(B - i)
    ans = list(set(ans))
    ans.sort()
    return ans
"""
QUESTION:
Gerald has n younger brothers and their number happens to be even. One day he bought n^2 candy bags. One bag has one candy, one bag has two candies, one bag has three candies and so on. In fact, for each integer k from 1 to n^2 he has exactly one bag with k candies. 

Help him give n bags of candies to each brother so that all brothers got the same number of candies.


-----Input-----

The single line contains a single integer n (n is even, 2 ≤ n ≤ 100) — the number of Gerald's brothers.


-----Output-----

Let's assume that Gerald indexes his brothers with numbers from 1 to n. You need to print n lines, on the i-th line print n integers — the numbers of candies in the bags for the i-th brother. Naturally, all these numbers should be distinct and be within limits from 1 to n^2. You can print the numbers in the lines in any order. 

It is guaranteed that the solution exists at the given limits.


-----Examples-----
Input
2

Output
1 4
2 3



-----Note-----

The sample shows Gerald's actions if he has two brothers. In this case, his bags contain 1, 2, 3 and 4 candies. He can give the bags with 1 and 4 candies to one brother and the bags with 2 and 3 to the other brother.
"""

def distribute_candies(n: int) -> list[list[int]]:
    """
    Distributes n^2 candy bags among n brothers such that each brother gets n bags 
    with distinct numbers of candies, and all brothers get the same total number of candies.

    Parameters:
    n (int): The number of brothers (n is even and 2 ≤ n ≤ 100).

    Returns:
    list[list[int]]: A list of n lists, each containing n integers representing the 
                     number of candies in the bags for each brother.
    """
    # Create a matrix to store the candy bags
    mx = [[0] * n for _ in range(n)]
    
    # Fill the matrix with candy bag numbers
    for i in range(n):
        for j in range(n):
            mx[i][j] = i * n + j + 1
    
    # Prepare the result list
    result = []
    
    # Distribute the candy bags to each brother
    for i in range(n):
        ans = []
        for j in range(n):
            ans.append(mx[j][(i + j) % n])
        result.append(ans)
    
    return result
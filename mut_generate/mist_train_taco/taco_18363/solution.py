"""
QUESTION:
The season for Snuke Festival has come again this year. First of all, Ringo will perform a ritual to summon Snuke. For the ritual, he needs an altar, which consists of three parts, one in each of the three categories: upper, middle and lower.
He has N parts for each of the three categories. The size of the i-th upper part is A_i, the size of the i-th middle part is B_i, and the size of the i-th lower part is C_i.
To build an altar, the size of the middle part must be strictly greater than that of the upper part, and the size of the lower part must be strictly greater than that of the middle part. On the other hand, any three parts that satisfy these conditions can be combined to form an altar.
How many different altars can Ringo build? Here, two altars are considered different when at least one of the three parts used is different.

-----Constraints-----
 - 1 \leq N \leq 10^5
 - 1 \leq A_i \leq 10^9(1\leq i\leq N)
 - 1 \leq B_i \leq 10^9(1\leq i\leq N)
 - 1 \leq C_i \leq 10^9(1\leq i\leq N)
 - All input values are integers.

-----Input-----
Input is given from Standard Input in the following format:
N
A_1 ... A_N
B_1 ... B_N
C_1 ... C_N

-----Output-----
Print the number of different altars that Ringo can build.

-----Sample Input-----
2
1 5
2 4
3 6

-----Sample Output-----
3

The following three altars can be built:
 - Upper: 1-st part, Middle: 1-st part, Lower: 1-st part
 - Upper: 1-st part, Middle: 1-st part, Lower: 2-nd part
 - Upper: 1-st part, Middle: 2-nd part, Lower: 2-nd part
"""

def count_possible_altars(N, A, B, C):
    """
    Counts the number of different altars that can be built from the given parts.

    Parameters:
    N (int): The number of parts in each category.
    A (list of int): List of sizes of the upper parts.
    B (list of int): List of sizes of the middle parts.
    C (list of int): List of sizes of the lower parts.

    Returns:
    int: The number of different altars that can be built.
    """
    # Sort the lists to facilitate binary search
    A.sort()
    B.sort()
    C.sort()
    
    import bisect
    sum = 0
    
    # Iterate over each middle part
    for b in B:
        # Find the number of upper parts that are strictly smaller than the current middle part
        b_num = bisect.bisect_left(A, b)
        # Find the number of lower parts that are strictly larger than the current middle part
        c_num = bisect.bisect_right(C, b)
        # Calculate the number of valid combinations for the current middle part
        sum += b_num * (len(C) - c_num)
    
    return sum
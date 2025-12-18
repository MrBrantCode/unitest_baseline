"""
QUESTION:
We have a sequence p = {p_1,\ p_2,\ ...,\ p_N} which is a permutation of {1,\ 2,\ ...,\ N}.
You can perform the following operation at most once: choose integers i and j (1 \leq i < j \leq N), and swap p_i and p_j. Note that you can also choose not to perform it.
Print YES if you can sort p in ascending order in this way, and NO otherwise.

-----Constraints-----
 - All values in input are integers.
 - 2 \leq N \leq 50
 - p is a permutation of {1,\ 2,\ ...,\ N}.

-----Input-----
Input is given from Standard Input in the following format:
N
p_1 p_2 ... p_N

-----Output-----
Print YES if you can sort p in ascending order in the way stated in the problem statement, and NO otherwise.

-----Sample Input-----
5
5 2 3 4 1

-----Sample Output-----
YES

You can sort p in ascending order by swapping p_1 and p_5.
"""

def can_sort_by_one_swap(p: list) -> str:
    """
    Determines if the given permutation sequence can be sorted in ascending order
    by performing at most one swap.

    Parameters:
    p (list): A list of integers representing the permutation sequence.

    Returns:
    str: "YES" if the sequence can be sorted by one swap, otherwise "NO".
    """
    sorted_p = sorted(p)
    cnt = 0
    
    for i in range(len(p)):
        if p[i] != sorted_p[i]:
            cnt += 1
    
    if cnt <= 2:
        return 'YES'
    else:
        return 'NO'
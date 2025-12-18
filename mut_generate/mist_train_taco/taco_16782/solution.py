"""
QUESTION:
Indraneel has to sort the books in his library. His library has one long shelf. His books are numbered $1$ through $N$ and he wants to rearrange the books so that they appear in the sequence $1,2, ..., N$.
He intends to do this by a sequence of moves. In each move he can pick up any book from the shelf and insert it at a different place in the shelf. Suppose Indraneel has $5$ books and they are initially arranged in the order
21453214532 \quad 1 \quad 4 \quad 5 \quad 3
Indraneel will rearrange this in ascending order by first moving book $1$ to the beginning of the shelf to get
12453124531 \quad 2 \quad 4 \quad 5 \quad 3
Then, moving book $3$ to position $3$, he gets
12345123451 \quad 2 \quad 3 \quad 4 \quad 5
Your task is to write a program to help Indraneel determine the minimum number of moves that are necessary to sort his book shelf.

-----Input:-----
The first line of the input will contain a single integer $N$ indicating the number of books in Indraneel's library. This is followed by a line containing a permutation of $1, 2, ..., N$ indicating the intial state of Indraneel's book-shelf.

-----Output:-----
A single integer indicating the minimum number of moves necessary to sort Indraneel's book-shelf.

-----Constraints:-----
- $1 \leq N \leq 200000$.
- You may also assume that in $50 \%$ of the inputs, $1 \leq N \leq 5000$.

-----Sample Input-----
5
2 1 4 5 3 

-----Sample Output-----
2
"""

def min_moves_to_sort_books(N: int, arr: list) -> int:
    """
    Calculate the minimum number of moves required to sort the bookshelf.

    Parameters:
    - N (int): The number of books on the shelf.
    - arr (list): The initial arrangement of the books on the shelf.

    Returns:
    - int: The minimum number of moves required to sort the bookshelf.
    """
    if sorted(arr) == arr:
        return 0
    
    l = [1] * N
    for i in range(N):
        for j in range(i):
            if arr[i] >= arr[j] and l[i] < l[j] + 1:
                l[i] = l[j] + 1
    
    return N - max(l)
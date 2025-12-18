"""
QUESTION:
Let us denote by f(x, m) the remainder of the Euclidean division of x by m.
Let A be the sequence that is defined by the initial value A_1=X and the recurrence relation A_{n+1} = f(A_n^2, M).
Find \displaystyle{\sum_{i=1}^N A_i}.

-----Constraints-----
 - 1 \leq N \leq 10^{10}
 - 0 \leq X < M \leq 10^5
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N X M

-----Output-----
Print \displaystyle{\sum_{i=1}^N A_i}.

-----Sample Input-----
6 2 1001

-----Sample Output-----
1369

The sequence A begins 2,4,16,256,471,620,\ldots Therefore, the answer is 2+4+16+256+471+620=1369.
"""

def sum_sequence_terms(N, X, M):
    """
    Calculate the sum of the first N terms of the sequence A defined by the initial value A_1 = X
    and the recurrence relation A_{n+1} = f(A_n^2, M), where f(x, m) is the remainder of the Euclidean division of x by m.

    Parameters:
    - N (int): The number of terms in the sequence to sum.
    - X (int): The initial value of the sequence.
    - M (int): The modulus value used in the recurrence relation.

    Returns:
    - int: The sum of the first N terms of the sequence.
    """
    yj = [X]
    lps = 0
    
    for i in range(N):
        an = yj[i] ** 2 % M
        if an in yj:
            lps = yj.index(an)
            break
        yj.append(an)
    
    blp = yj[:lps]
    lp = yj[lps:]
    
    ans = sum(blp) + sum(lp) * ((N - len(blp)) // len(lp)) + sum(lp[:(N - len(blp)) % len(lp)])
    
    return ans
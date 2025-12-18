"""
QUESTION:
When l is an odd number, the median of l numbers a_1, a_2, ..., a_l is the (\frac{l+1}{2})-th largest value among a_1, a_2, ..., a_l.

You are given N numbers X_1, X_2, ..., X_N, where N is an even number. For each i = 1, 2, ..., N, let the median of X_1, X_2, ..., X_N excluding X_i, that is, the median of X_1, X_2, ..., X_{i-1}, X_{i+1}, ..., X_N be B_i.

Find B_i for each i = 1, 2, ..., N.

Constraints

* 2 \leq N \leq 200000
* N is even.
* 1 \leq X_i \leq 10^9
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
X_1 X_2 ... X_N


Output

Print N lines. The i-th line should contain B_i.

Examples

Input

4
2 4 4 3


Output

4
3
3
4


Input

2
1 2


Output

2
1


Input

6
5 5 4 4 3 3


Output

4
4
4
4
4
4
"""

def calculate_medians(N, X):
    # Sort the list of elements
    X_sort = sorted(X)
    
    # Calculate the median values for the list excluding one element
    med_n = X_sort[N // 2 - 1]
    med_p = X_sort[N // 2]
    
    # Initialize the result list
    result = []
    
    # Determine the median for each element in the original list
    for i in range(N):
        if X[i] <= med_n:
            result.append(med_p)
        else:
            result.append(med_n)
    
    return result
"""
QUESTION:
Blob is a computer science student. He recently got an internship from Chef's enterprise. Along with the programming he has various other skills too like graphic designing, digital marketing and social media management. Looking at his skills Chef has provided him different tasks A[1…N] which have their own scores. Blog wants to maximize the  value of the expression A[d]-A[c]+A[b]-A[a] such that d>c>b>a.

Can you help him in this?

-----Input:-----
- The first line contain the integer N
- The second line contains N space separated integers representing A[1], A[2] … A[N]

-----Output:-----
The maximum score that is possible

-----Constraints-----
- $4 \leq N \leq 10^4$
- $0 \leq A[i] \leq 10^5$

-----Sample Input:-----
6

3 9 10 1 30 40

-----Sample Output:-----
46
"""

def maximize_expression_value(arr):
    """
    Calculate the maximum value of the expression A[d] - A[c] + A[b] - A[a]
    such that d > c > b > a.

    Parameters:
    arr (list of int): The list of integers representing the scores of the tasks.

    Returns:
    int: The maximum value of the expression.
    """
    if len(arr) < 4:
        raise ValueError("The array must contain at least 4 elements.")
    
    fn = [float('-inf')] * (len(arr) + 1)
    sn = [float('-inf')] * len(arr)
    tn = [float('-inf')] * (len(arr) - 1)
    fon = [float('-inf')] * (len(arr) - 2)
    
    for i in reversed(range(len(arr))):
        fn[i] = max(fn[i + 1], arr[i])
    
    for i in reversed(range(len(arr) - 1)):
        sn[i] = max(sn[i + 1], fn[i + 1] - arr[i])
    
    for i in reversed(range(len(arr) - 2)):
        tn[i] = max(tn[i + 1], sn[i + 1] + arr[i])
    
    for i in reversed(range(len(arr) - 3)):
        fon[i] = max(fon[i + 1], tn[i + 1] - arr[i])
    
    return fon[0]
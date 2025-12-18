"""
QUESTION:
Dexter, being irritated by DD, gave her a lucrative game to play to keep her busy.
There are $N$ bags numbered $1$ to $N$. The $i_{th}$ bag contains $A_i$ coins. The bags are placed in a circular order such that the $N_{th}$ bag is adjacent to the $1^{st}$ bag. 
DD can select $K$ consecutive adjacent bags and take all the coins in them.   Help her find the maximum number of coins she can take by making the ideal choice.
Note that the selected bags must be consecutive. Since they are placed in circular order, bag number $1$ and $N$ are considered to be consecutive.

-----Input:-----
- First-line will contain $T$, the number of test cases. Then the test cases follow. 
- First-line contains $N$ and $K$.
- Second-line contains $N$ numbers $A_1, A_2,...,A_N$,  

-----Output:-----
For each test case, output in a single line, the maximum money that can be collected by DD.

-----Constraints-----
- $1 \leq T \leq 100$
- $5 \leq N \leq 10^5$
- $1 \leq K < N$
- $1 \leq A_i \leq 10^5$
Sum of $N$ over all test cases is less than $10^6$

-----Sample Input:-----
1
5 3
8 6 9 4 10

-----Sample Output:-----
24

-----EXPLANATION:-----
The ideal choice would be to take the last bag with $10$ coins and the first $2$ bags with $8$ and $6$ coins.
"""

def max_circular_sum(arr, n, k):
    if n < k:
        return 'Invalid'
    
    # Calculate the initial sum of the first k elements
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    # Iterate over the array to find the maximum sum
    for i in range(1, n):
        current_sum = current_sum - arr[i - 1] + arr[(i + k - 1) % n]
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum
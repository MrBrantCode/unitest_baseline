"""
QUESTION:
There are N blocks arranged in a row, numbered 1 to N from left to right. Each block has a weight, and the weight of Block i is A_i. Snuke will perform the following operation on these blocks N times:

* Choose one block that is still not removed, and remove it. The cost of this operation is the sum of the weights of the blocks that are connected to the block being removed (including itself). Here, two blocks x and y ( x \leq y ) are connected when, for all z ( x \leq z \leq y ), Block z is still not removed.



There are N! possible orders in which Snuke removes the blocks. For all of those N! orders, find the total cost of the N operations, and calculate the sum of those N! total costs. As the answer can be extremely large, compute the sum modulo 10^9+7.

Constraints

* 1 \leq N \leq 10^5
* 1 \leq A_i \leq 10^9
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
A_1 A_2 ... A_N


Output

For all of the N! orders, find the total cost of the N operations, and print the sum of those N! total costs, modulo 10^9+7.

Examples

Input

2
1 2


Output

9


Input

4
1 1 1 1


Output

212


Input

10
1 2 4 8 16 32 64 128 256 512


Output

880971923
"""

MOD = 10 ** 9 + 7

def calculate_total_cost(N, A):
    prodasc = [1] * (N + 1)
    prodesc = [1] * (N + 1)
    
    for i in range(N):
        prodasc[i + 1] = prodasc[i] * (i + 1) % MOD
        prodesc[i + 1] = prodesc[i] * (N - i) % MOD
    
    inv = [1] * (N + 1)
    for i in range(1, N + 1):
        inv[i] = prodasc[i - 1] * prodesc[N - i] % MOD
    
    cumsum = [0] * N
    for i in range(1, N):
        cumsum[i] = (cumsum[i - 1] + inv[i + 1]) % MOD
    
    ans = 0
    for i in range(N):
        ans = (ans + A[i] * (prodasc[N] + cumsum[i] + cumsum[N - 1 - i])) % MOD
    
    return ans
"""
QUESTION:
Chef is making polygon cakes in his kitchen today! 
Since the judge panel is very strict, Chef's cakes must be beautiful and have sharp and precise $internal$ angles in arithmetic progression. 
Given the number of sides, $N$, of the cake Chef is baking today and also the measure of its first angle(smallest angle), $A$, find the measure of the $K^{th}$ angle.

-----Input:-----
- The first line contains a single integer $T$, the number of test cases. 
- The next $T$ lines contain three space separated integers $N$, $A$ and $K$, the number of sides of polygon, the first angle and the $K^{th}$ angle respectively. 

-----Output:-----
For each test case, print two space separated integers $X$ and $Y$, such that the $K^{th}$ angle can be written in the form of $X/Y$ and $gcd(X, Y) = 1$

-----Constraints-----
- $1 \leq T \leq 50$
- $3 \leq N \leq 1000$
- $1 \leq A \leq 1000000000$
- $1 \leq K \leq N$
- It is guaranteed the answer is always valid.

-----Sample Input:-----
1
3 30 2

-----Sample Output:-----
60 1
"""

def calculate_kth_angle(T, test_cases):
    def gcd(A, B):
        if B == 0:
            return A
        else:
            return gcd(B, A % B)
    
    results = []
    for n, a, k in test_cases:
        num = a * (n * (n - 1)) + (k - 1) * (360 * (n - 2) - 2 * a * n)
        den = n * (n - 1)
        gcd_value = gcd(num, den)
        results.append((num // gcd_value, den // gcd_value))
    
    return results
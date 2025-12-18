"""
QUESTION:
The Chef once decided to prepare some nice dishes on his birthday. There are N items kept on his shelf linearly from position 1 to N. Taste of the i-th item is denoted by a integer Ai.

He wants to make Q dishes. A dish will be made using some ingredients in the continuous range AL, AL + 1, , , AR (1-base indexing). Quality of the dish will be determined by the ingredient with minimum taste.

Chef wants help of his assistant Rupsa to find out sum and product of qualities of the dishes. As product of the qualities of the dishes could be very large, print it modulo 109 + 7. Also, you are given an integer K and you are assured that for each dish, the size of continuous range of the ingredients (i.e. R - L + 1) will always lie between K and 2 * K, both inclusive.

Method of generation of Array A 

You are given non-negative integer parameters a, b, c, d, e, f, r, s, t, m, A[1]

for x = 2 to N:
	if(t^x mod s  <= r)        // Here t^x signifies "t to the power of x"
		A[x] = (a*A[x-1]^2 + b*A[x-1] + c) mod m
	else
		A[x] = (d*A[x-1]^2 + e*A[x-1] + f) mod m

Method of generation of range of ingredients for Q dishes 

You are given non-negative integer parameters L1, La, Lc, Lm, D1, Da, Dc, Dm

for i = 1 to Q:
	L1 = (La * L1 + Lc) mod Lm;
	D1 = (Da * D1 + Dc) mod Dm; 
	L = L1 + 1;
	R = min(L + K - 1 + D1, N);

-----Input-----
- The first line contains three integers N, K and Q.
- The second line contains the integers a, b, c, d, e, f, r, s, t, m, and A[1].
- Then third line contains the integers L1, La, Lc, Lm, D1, Da, Dc, and Dm

-----Output-----
Output two space separated integers:

- The sum of qualities of the dishes.
- The product of qualities of the dishes modulo 109+7.

-----Constraints-----
- 1 ≤ N, Q ≤ 107
- 1 ≤ K ≤ N
- 0 ≤ a, b, c, d, e, f, r, s, t, m, A[1] ≤ 109+7
- 1 ≤ Lm ≤ N - K + 1
- 1 ≤ Dm ≤ K + 1
- 1 ≤ La, Lc ≤ Lm
- 1 ≤ Da, Dc ≤ Dm
- 1 ≤ L1 ≤ N
- 1 ≤ D1 ≤ K

-----Sub tasks-----
- Subtask #1: 1 ≤ N, Q ≤ 1000 (10 points)
- Subtask #2: 1 ≤ Q ≤ 104 (20 points)
- Subtask #3: original constraints (70 points)

-----Example-----
Input:
4 2 1
1 1 1 1 1 1 1 1 1 100 1 
1 1 1 3 1 1 1 2

Output:
13 13

-----Explanation-----
- The array A comes out to be {1, 3, 13, 83} and the first dish has L = 3 and R = 4. The minimum in this range is 13, thus the sum and product both are 13 and hence the answer.

-----Note-----
Multiplier for C# and Java have been reduced to 1.5 instead of 2.
"""

def calculate_dish_qualities(N, K, Q, a, b, c, d, e, f, r, s, t, m, A1, L1, La, Lc, Lm, D1, Da, Dc, Dm):
    mod = 10**9 + 7
    A = [0] * N
    A[0] = A1
    
    # Generate array A
    for x in range(1, N):
        if pow(t, x + 1, s) <= r:
            A[x] = (a * pow(A[x - 1], 2, m) + b * A[x - 1] + c) % m
        else:
            A[x] = (d * pow(A[x - 1], 2, m) + e * A[x - 1] + f) % m
    
    # Function to find minimum in sliding window
    def SRMQ(arr, k):
        from collections import deque
        n = len(arr)
        ans = [None] * n
        deque = deque()
        for i in range(n):
            while deque and deque[-1] > arr[i]:
                deque.pop()
            deque.append(arr[i])
            if i >= k and arr[i - k] == deque[0]:
                deque.popleft()
            if i >= k - 1:
                ans[i - k + 1] = deque[0]
        return ans
    
    v = SRMQ(A, K)
    
    sum_of_qualities = 0
    product_of_qualities = 1
    
    for _ in range(Q):
        L1 = (La * L1 + Lc) % Lm
        D1 = (Da * D1 + Dc) % Dm
        L = L1 + 1
        R = min(L + K - 1 + D1, N)
        z = min(v[L - 1], v[R - K])
        sum_of_qualities += z
        product_of_qualities = product_of_qualities * z % mod
    
    return sum_of_qualities, product_of_qualities
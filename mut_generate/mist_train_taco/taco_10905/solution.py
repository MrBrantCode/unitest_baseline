"""
QUESTION:
Chef wants to impress Chefina by giving her the maximum number of gifts possible.

Chef is in a gift shop having N items where the cost of the i^{th} item is equal to A_{i}.
Chef has K amount of money and a 50 \% off discount coupon that he can use for at most one of the items he buys.

If the cost of an item is equal to X, then, after applying the coupon on that item, Chef only has to pay {\bf \lceil \frac{X}{2} \right\rceil} (rounded up to the nearest integer) amount for that item.

Help Chef find the maximum number of items he can buy with K amount of money and a 50 \% discount coupon given that he can use the coupon on at most one item.

------ Input Format ------ 

- The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains two space-separated integers N and K.
- The next line contains N space-separated integers, where the i^{th} integer A_{i} denotes the cost of the i^{th} item.

------ Output Format ------ 

For each test case, print a single line containing one integer ― the maximum number of items Chef can buy.

------ Constraints ------ 

$1 ≤ T ≤ 10^{3}$
$1 ≤ N ≤ 10^{5}$
$1 ≤ A_{i} ≤ 10^{9}$
$0 ≤ K ≤ 10^{9}$
- Sum of $N$ over all test cases does not exceed $2\cdot10^{5}$.

----- Sample Input 1 ------ 
3
1 4
5
3 15
4 4 5
3 10
6 7 4
----- Sample Output 1 ------ 
1
3
2
----- explanation 1 ------ 
Test case $1$: After applying the discount, Chef can buy the only available item at ${\lceil \frac{5}{2} \right\rceil} = 3$.

Test case $2$: Chef can buy all three items even without using the coupon.

Test case $3$: After applying coupon on the third item, Chef can buy the second and the third item at $7 + {\lceil \frac{4}{2} \right\rceil} = $ $ 7 + 2 = 9$.  
It is not possible for Chef to buy more than two items.
"""

import math

def max_gifts_with_discount(N, K, A):
    def apply_discount(cost):
        return math.ceil(cost / 2)
    
    A.sort()
    max_items = 0
    total_cost = 0
    
    # First, try to buy as many items as possible without using the coupon
    for cost in A:
        if total_cost + cost <= K:
            total_cost += cost
            max_items += 1
        else:
            break
    
    # If we can't buy any more items without the coupon, try using the coupon on the most expensive item we can afford
    if max_items < N:
        for i in range(max_items, N):
            discounted_cost = apply_discount(A[i])
            if total_cost - A[max_items - 1] + discounted_cost <= K:
                max_items += 1
                break
    
    return max_items
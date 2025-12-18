"""
QUESTION:
Winter is coming, along with winter comes the white walkers who may destroy every human life on the planet. Only Brandon can stop it from happening but he is kidnapped by the White Walkers. His brother Jon wishes to set him free so that they can stop the destruction.
To set his brother free Jon has to kill the White Walkers who stand against the cave where his brother is kept as slave. Jon has somehow managed to place few of his men among the White Walkers who may help him in rescuing Brandon. Jon has the power to kill at most k White Walkers at a time, after which he would need one of his friends to help him gain back his power. Every time Jon meets any of his friend his power is restored to k.
The n White Walkers (all assumed to be White Walkers apparently) stand in the given order denoted by some numbers. The ith person will have the number a[i] associated with them. Jon can identify his friend with the help of the numbers. If the number is prime, it is Jon’s friend who stands there else it’s the White Walkers.
Given the order, comment whether Jon will be able to rescue his brother or not.
Example 1:
Input:
n = 5, k = 2
Arr = {6 , 3, 4, 5, 6}
Output: 1
Explaination: Jon can kill at most 2 White 
Walkers before reaching his friend. 
He kills the first (6) and he finds his 
friend (3) then again he kills one (4) and 
finds his friend (5). He now only has to kill 
one White Walker (6) to reach his brother.
Example 2:
Input:
n = 6, k = 3
Arr = {1, 2, 10, 4, 6, 8}
Output: 0
Explaination: same logic as the previous one.
Your Task:
You don't need to read input or print anything. Your task is to complete the function ableTorescue() which takes the array Arr[] and its size n and k as input parameters and returns 1 if Jon is able to rescue his brother, 0 if he cannot.
Expected Time Complexity: O(nloglogn)
Expected Auxiliary Space: O(n)
Constraints:
1 <= k <= n <=10^{5}
1 <= Arr[i] <= 10^{5}
"""

def able_to_rescue(Arr, n, k):
    life = k
    for i in range(n):
        if is_prime(Arr[i]):
            life = k
        else:
            life -= 1
        if life < 0:
            break
    if life < 0:
        return 0
    else:
        return 1

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
"""
QUESTION:
ATMs of a well-known bank of a small country are arranged so that they can not give any amount of money requested by the user. Due to the limited size of the bill dispenser (the device that is directly giving money from an ATM) and some peculiarities of the ATM structure, you can get at most k bills from it, and the bills may be of at most two distinct denominations.

For example, if a country uses bills with denominations 10, 50, 100, 500, 1000 and 5000 burles, then at k = 20 such ATM can give sums 100 000 burles and 96 000 burles, but it cannot give sums 99 000 and 101 000 burles.

Let's suppose that the country uses bills of n distinct denominations, and the ATM that you are using has an unlimited number of bills of each type. You know that during the day you will need to withdraw a certain amount of cash q times. You know that when the ATM has multiple ways to give money, it chooses the one which requires the minimum number of bills, or displays an error message if it cannot be done. Determine the result of each of the q of requests for cash withdrawal.

Input

The first line contains two integers n, k (1 ≤ n ≤ 5000, 1 ≤ k ≤ 20).

The next line contains n space-separated integers ai (1 ≤ ai ≤ 107) — the denominations of the bills that are used in the country. Numbers ai follow in the strictly increasing order.

The next line contains integer q (1 ≤ q ≤ 20) — the number of requests for cash withdrawal that you will make.

The next q lines contain numbers xi (1 ≤ xi ≤ 2·108) — the sums of money in burles that you are going to withdraw from the ATM.

Output

For each request for cash withdrawal print on a single line the minimum number of bills it can be done, or print  - 1, if it is impossible to get the corresponding sum.

Examples

Input

6 20
10 50 100 500 1000 5000
8
4200
100000
95000
96000
99000
10100
2015
9950


Output

6
20
19
20
-1
3
-1
-1


Input

5 2
1 2 3 5 8
8
1
3
5
7
9
11
13
15


Output

1
1
1
2
2
2
2
-1
"""

def atm_withdrawal(n, k, denominations, queries):
    # Create a dictionary to store the minimum number of bills for each possible sum
    pares = {}
    
    # Populate the dictionary with the minimum number of bills for each sum
    for a in denominations:
        for i in range(k):
            p = (i + 1) * a
            if p not in pares or i + 1 < pares[p]:
                pares[p] = i + 1
    
    # Initialize a large number to use for comparison
    m = 1000000000
    
    # Process each query
    results = []
    for x in queries:
        ans = 1000
        minimo = m
        
        # Check each possible sum in the dictionary
        for (plata, deuda) in pares.items():
            if plata == x:
                if deuda <= k:
                    if deuda < minimo:
                        minimo = deuda
            else:
                r = x - plata
                if r in pares:
                    if deuda + pares[r] < minimo:
                        if deuda + pares[r] <= k:
                            minimo = deuda + pares[r]
        
        # If no valid combination was found, set result to -1
        if minimo == m:
            results.append(-1)
        else:
            results.append(minimo)
    
    return results
"""
QUESTION:
It is known that there are k fish species in the polar ocean, numbered from 1 to k. They are sorted by non-decreasing order of their weight, which is a positive number. Let the weight of the i-th type of fish be wi, then 0 < w1 ≤ w2 ≤ ... ≤ wk holds.

Polar bears Alice and Bob each have caught some fish, and they are guessing who has the larger sum of weight of the fish he/she's caught. Given the type of the fish they've caught, determine whether it is possible that the fish caught by Alice has a strictly larger total weight than Bob's. In other words, does there exist a sequence of weights wi (not necessary integers), such that the fish caught by Alice has a strictly larger total weight?

Input

The first line contains three integers n, m, k (1 ≤ n, m ≤ 105, 1 ≤ k ≤ 109) — the number of fish caught by Alice and Bob respectively, and the number of fish species.

The second line contains n integers each from 1 to k, the list of fish type caught by Alice. The third line contains m integers each from 1 to k, the list of fish type caught by Bob.

Note that one may have caught more than one fish for a same species.

Output

Output "YES" (without quotes) if it is possible, and "NO" (without quotes) otherwise.

Examples

Input

3 3 3
2 2 2
1 1 3


Output

YES


Input

4 7 9
5 2 7 3
3 5 2 7 3 8 7


Output

NO

Note

In the first sample, if w1 = 1, w2 = 2, w3 = 2.5, then Alice has a total of 2 + 2 + 2 = 6 weight units, while Bob only has 1 + 1 + 2.5 = 4.5.

In the second sample, the fish that Alice caught is a subset of Bob's. Therefore, the total weight of Bob’s fish is always not less than the total weight of Alice’s fish.
"""

def can_alice_have_larger_total_weight(n, m, k, alice_fish, bob_fish):
    alice_fish.sort()
    bob_fish.sort()
    
    balance = 0
    i = n - 1
    j = m - 1
    
    while i >= 0 and j >= 0:
        if alice_fish[i] > bob_fish[j]:
            balance += 1
            i -= 1
        elif alice_fish[i] < bob_fish[j]:
            balance -= 1
            j -= 1
        else:
            i -= 1
            j -= 1
        
        if balance > 0:
            break
    
    if i + 1 + balance > 0:
        return 'YES'
    else:
        return 'NO'
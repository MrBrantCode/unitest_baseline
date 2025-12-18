"""
QUESTION:
Sometimes Sergey visits fast food restaurants. Today he is going to visit the one called PizzaKing.
Sergey wants to buy N meals, which he had enumerated by integers from 1 to N. He knows that the meal i costs Ci rubles. He also knows that there are M meal sets in the restaurant.
The meal set is basically a set of meals, where you pay Pj burles and get Qj meals - Aj, 1, Aj, 2, ..., Aj, Qj.
Sergey has noticed that sometimes he can save money by buying the meals in the meal sets instead of buying each one separately. And now he is curious about what is the smallest amount of rubles he needs to spend to have at least one portion of each of the meals.

-----Input-----
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a pair of integer numbers N and M denoting the number of meals and the number of the meal sets.
The second line contains N space-separated integers C1, C2, ..., CN denoting the costs of the meals, bought separately.
Each of the following M lines starts with a pair of integer numbers Pi and Qi, denoting the cost of the meal set and the number of meals in it, followed with the integer numbers Ai, 1 Ai, 2, ..., Ai, Qi denoting the meal numbers.

-----Output-----
For each test case, output a single line containing the minimal total amount of money Sergey needs to spend in order to have at least one portion of each meal.

-----Constraints-----
- 1 ≤ Pi, Ci ≤ 106
- 1 ≤ M ≤ min{2N, 2 × 100000}
- No meal appears in the set twice or more times.
- Subtask 1 (16 points): 1 ≤ T ≤ 103, 1 ≤ N ≤ 8
- Subtask 2 (23 points): For each test file, either 1 ≤ T ≤ 10, 1 ≤ N ≤ 12 or the constraints for Subtask 1 are held.
- Subtask 3 (61 points): For each test file, either T = 1, 1 ≤ N ≤ 18 or the constraints for Subtask 1 or 2 are held.

-----Example-----
Input:1
3 3
3 5 6
11 3 1 2 3
5 2 1 2
5 2 1 3

Output:10

-----Explanation-----
Example case 1. If Sergey buys all the meals separately, it would cost him 3 + 5 + 6 = 14 rubles. He can buy all of them at once by buying the first meal set, which costs for 11 rubles, but the optimal strategy would be either to buy the second and the third meal set, thus, paying 5 + 5 = 10 rubles, or to buy the third meal set and the second meal separately by paying the same amount of 10 rubles.
"""

def calculate_minimum_cost(T, test_cases):
    results = []
    
    for t in range(T):
        N, M, C, meal_sets = test_cases[t]
        
        dp1 = [1000000000.0] * ((1 << N) + 1)
        
        for i in range(N):
            dp1[1 << i] = C[i]
        
        dp1[(1 << N) - 1] = min(dp1[(1 << N) - 1], sum(C))
        
        for i in range(M):
            P, Q, A = meal_sets[i]
            mask = 0
            for j in A:
                mask = mask | 1 << (j - 1)
            dp1[mask] = min(dp1[mask], P)
        
        for i in range((1 << N) - 1, -1, -1):
            for j in range(N):
                if i & 1 << j:
                    dp1[i ^ 1 << j] = min(dp1[i ^ 1 << j], dp1[i])
        
        dp2 = [1000000000.0] * ((1 << N) + 1)
        dp2[0] = 0
        
        for i in range(1 << N):
            submask = i
            while submask > 0:
                dp2[i] = min(dp2[i], dp2[i ^ submask] + dp1[submask])
                submask = submask - 1 & i
        
        results.append(dp2[(1 << N) - 1])
    
    return results
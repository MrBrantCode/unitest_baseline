"""
QUESTION:
Bash has set out on a journey to become the greatest Pokemon master. To get his first Pokemon, he went to Professor Zulu's Lab. Since Bash is Professor Zulu's favourite student, Zulu allows him to take as many Pokemon from his lab as he pleases.

But Zulu warns him that a group of k > 1 Pokemon with strengths {s_1, s_2, s_3, ..., s_{k}} tend to fight among each other if gcd(s_1, s_2, s_3, ..., s_{k}) = 1 (see notes for gcd definition).

Bash, being smart, does not want his Pokemon to fight among each other. However, he also wants to maximize the number of Pokemon he takes from the lab. Can you help Bash find out the maximum number of Pokemon he can take? 

Note: A Pokemon cannot fight with itself.


-----Input-----

The input consists of two lines.

The first line contains an integer n (1 ≤ n ≤ 10^5), the number of Pokemon in the lab.

The next line contains n space separated integers, where the i-th of them denotes s_{i} (1 ≤ s_{i} ≤ 10^5), the strength of the i-th Pokemon.


-----Output-----

Print single integer — the maximum number of Pokemons Bash can take.


-----Examples-----
Input
3
2 3 4

Output
2

Input
5
2 3 4 6 7

Output
3



-----Note-----

gcd (greatest common divisor) of positive integers set {a_1, a_2, ..., a_{n}} is the maximum positive integer that divides all the integers {a_1, a_2, ..., a_{n}}.

In the first sample, we can take Pokemons with strengths {2, 4} since gcd(2, 4) = 2.

In the second sample, we can take Pokemons with strengths {2, 4, 6}, and there is no larger group with gcd ≠ 1.
"""

def max_non_fighting_pokemon(n, strengths):
    M = 10 ** 5
    prime_factor = [set() for _ in range(M + 1)]
    
    # Populate prime factors for each number up to M
    for p in range(2, M + 1):
        if prime_factor[p] != set():
            continue
        for i in range(p, M + 1, p):
            prime_factor[i].add(p)
    
    cnt = [0] * (M + 1)
    
    # Count the occurrences of each prime factor in the strengths
    for s in strengths:
        for p in prime_factor[s]:
            cnt[p] += 1
    
    # The maximum number of Pokemon that can be taken is the maximum count of any prime factor
    return max(1, max(cnt))
"""
QUESTION:
Consider a sequence $S_n$ defined by the initial condition $S_0 = 290797$ and the recursive relation $S_n = S_{n - 1}^2 \bmod 50515093$ for $n > 0$. Write a function `calculate_steps(N)` to compute the total number of steps required to arrange the bowls in a non-descending order of beans, where initially each bowl $n$ contains $S_n$ beans. The function should take an integer `N` as input and return the total number of steps. The sequence $S_n$ can be assumed to be extremely chaotic and a new maximum can only appear in a position that is a perfect square.
"""

def calculate_steps(N):
    MOD = 50515093
    s = [290797]
    max_positions = [0]

    for i in range(1, N):
        s.append((s[-1] ** 2) % MOD)
        if s[-1] > s[max_positions[-1]]:
            max_positions.append(i)

    ans = sum((max_positions[i+1] - max_positions[i]) * s[max_positions[i]] for i in range(len(max_positions) - 1))
    ans += (N - max_positions[-1]) * s[max_positions[-1]]
    return ans
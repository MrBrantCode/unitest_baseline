"""
QUESTION:
In a public bath, there is a shower which emits water for T seconds when the switch is pushed.

If the switch is pushed when the shower is already emitting water, from that moment it will be emitting water for T seconds. Note that it does not mean that the shower emits water for T additional seconds.

N people will push the switch while passing by the shower. The i-th person will push the switch t_i seconds after the first person pushes it.

How long will the shower emit water in total?

Constraints

* 1 ≤ N ≤ 200,000
* 1 ≤ T ≤ 10^9
* 0 = t_1 < t_2 < t_3 < , ..., < t_{N-1} < t_N ≤ 10^9
* T and each t_i are integers.

Input

Input is given from Standard Input in the following format:


N T
t_1 t_2 ... t_N


Output

Assume that the shower will emit water for a total of X seconds. Print X.

Examples

Input

2 4
0 3


Output

7


Input

2 4
0 5


Output

8


Input

4 1000000000
0 1000 1000000 1000000000


Output

2000000000


Input

1 1
0


Output

1


Input

9 10
0 3 5 7 100 110 200 300 311


Output

67
"""

def calculate_shower_duration(N, T, t):
    # Initialize the total duration with the first push
    total_duration = T
    
    # Iterate through the list of times to calculate the total duration
    for i in range(1, N):
        interval = t[i] - t[i - 1]
        total_duration += min(T, interval)
    
    return total_duration
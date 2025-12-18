"""
QUESTION:
Petya and his friend, robot Petya++, like to solve exciting math problems.

One day Petya++ came up with the numbers $n$ and $x$ and wrote the following equality on the board: $$n\ \&\ (n+1)\ \&\ \dots\ \&\ m = x,$$ where $\&$ denotes the bitwise AND operation . Then he suggested his friend Petya find such a minimal $m$ ($m \ge n$) that the equality on the board holds.

Unfortunately, Petya couldn't solve this problem in his head and decided to ask for computer help. He quickly wrote a program and found the answer.

Can you solve this difficult problem?


-----Input-----

Each test contains multiple test cases. The first line contains the number of test cases $t$ ($1 \le t \le 2000$). The description of the test cases follows.

The only line of each test case contains two integers $n$, $x$ ($0\le n, x \le 10^{18}$).


-----Output-----

For every test case, output the smallest possible value of $m$ such that equality holds.

If the equality does not hold for any $m$, print $-1$ instead.

We can show that if the required $m$ exists, it does not exceed $5 \cdot 10^{18}$.


-----Examples-----

Input
5
10 8
10 10
10 42
20 16
1000000000000000000 0
Output
12
10
-1
24
1152921504606846976


-----Note-----

In the first example, $10\ \&\ 11 = 10$, but $10\ \&\ 11\ \&\ 12 = 8$, so the answer is $12$.

In the second example, $10 = 10$, so the answer is $10$.

In the third example, we can see that the required $m$ does not exist, so we have to print $-1$.
"""

def find_minimal_m(n, x):
    if n == x:
        return n
    
    n_binary = format(n, 'b')
    x_binary = format(x, 'b')
    
    # Ensure both binary strings are of the same length
    if len(x_binary) < len(n_binary):
        x_binary = '0' * (len(n_binary) - len(x_binary)) + x_binary
    if len(n_binary) < len(x_binary):
        n_binary = '0' * (len(x_binary) - len(n_binary)) + n_binary
    
    diff_idx = 0
    while n_binary[diff_idx] == x_binary[diff_idx]:
        diff_idx += 1
    
    if x_binary[diff_idx] == '1':
        return -1
    
    if '1' in x_binary[diff_idx:]:
        return -1
    
    if diff_idx == 0:
        return int('1' + '0' * len(n_binary), 2)
    
    if n_binary[diff_idx - 1] != '0':
        return -1
    
    return int(n_binary[:diff_idx - 1] + '1' + '0' * (len(n_binary) - diff_idx), 2)
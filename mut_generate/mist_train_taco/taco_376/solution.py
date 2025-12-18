"""
QUESTION:
Polycarp is reading a book consisting of $n$ pages numbered from $1$ to $n$. Every time he finishes the page with the number divisible by $m$, he writes down the last digit of this page number. For example, if $n=15$ and $m=5$, pages divisible by $m$ are $5, 10, 15$. Their last digits are $5, 0, 5$ correspondingly, their sum is $10$.

Your task is to calculate the sum of all digits Polycarp has written down.

You have to answer $q$ independent queries.


-----Input-----

The first line of the input contains one integer $q$ ($1 \le q \le 1000$) — the number of queries.

The following $q$ lines contain queries, one per line. Each query is given as two integers $n$ and $m$ ($1 \le n, m \le 10^{16}$) — the number of pages in the book and required divisor, respectively.


-----Output-----

For each query print the answer for it — the sum of digits written down by Polycarp.


-----Example-----
Input
7
1 1
10 1
100 3
1024 14
998244353 1337
123 144
1234312817382646 13

Output
1
45
153
294
3359835
0
427262129093995
"""

def calculate_digit_sum(n: int, m: int) -> int:
    # Calculate the last digit of m
    last_digit = m % 10
    
    # Create a list of sums of last digits for multiples of m up to 10
    l = [last_digit]
    for i in range(1, 10):
        l.append((l[-1] + last_digit) % 10)
    
    # Calculate the total number of multiples of m up to n
    a = n // m
    
    # Calculate the number of complete cycles of 10 multiples
    b = a // 10
    
    # Calculate the sum of digits for complete cycles
    ans = b * sum(l)
    
    # Add the sum of digits for the remaining multiples
    for i in range(a % 10):
        ans += l[i]
    
    return ans
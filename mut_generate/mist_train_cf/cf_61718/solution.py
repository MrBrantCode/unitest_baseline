"""
QUESTION:
Define a function `count_sequences(max_start, cnt)` that determines the quantity of sequences, with an initial number less than `max_start`, that consist of exactly `cnt` unique terms, where each term in the sequence is the sum of the factorial of the digits of the previous term.
"""

import math

fact = [math.factorial(i) for i in range(10)]
lengths = [0] * 3000000
lengths[169] = lengths[363601] = lengths[1454] = 3
lengths[871] = lengths[45361] = 2
lengths[872] = lengths[45362] = 2

def next_fact(n):
    s = 0
    while n > 0:
        s += fact[n % 10]
        n //= 10
    return s

def get_sequence(n):
    seen = set()
    while n not in seen and n < 3000000 and lengths[n] == 0:
        seen.add(n)
        n = next_fact(n)

    l = 1 + (0 if n >= 3000000 else lengths[n])

    for m in seen:
        lengths[m] = l
        l -= 1

def count_sequences(max_start, cnt):
    num_seq = 0
    for i in range(1, max_start):
        if lengths[i] == 0:
            get_sequence(i)
        if lengths[i] == cnt:
            num_seq += 1
    return num_seq
"""
QUESTION:
Alice and Bob begin their day with a quick game. They first choose a starting number X_0 ≥ 3 and try to reach one million by the process described below. 

Alice goes first and then they take alternating turns. In the i-th turn, the player whose turn it is selects a prime number smaller than the current number, and announces the smallest multiple of this prime number that is not smaller than the current number.

Formally, he or she selects a prime p < X_{i} - 1 and then finds the minimum X_{i} ≥ X_{i} - 1 such that p divides X_{i}. Note that if the selected prime p already divides X_{i} - 1, then the number does not change.

Eve has witnessed the state of the game after two turns. Given X_2, help her determine what is the smallest possible starting number X_0. Note that the players don't necessarily play optimally. You should consider all possible game evolutions.


-----Input-----

The input contains a single integer X_2 (4 ≤ X_2 ≤ 10^6). It is guaranteed that the integer X_2 is composite, that is, is not prime.


-----Output-----

Output a single integer — the minimum possible X_0.


-----Examples-----
Input
14

Output
6

Input
20

Output
15

Input
8192

Output
8191



-----Note-----

In the first test, the smallest possible starting number is X_0 = 6. One possible course of the game is as follows:   Alice picks prime 5 and announces X_1 = 10  Bob picks prime 7 and announces X_2 = 14. 

In the second case, let X_0 = 15.   Alice picks prime 2 and announces X_1 = 16  Bob picks prime 5 and announces X_2 = 20.
"""

import math

# List of prime numbers up to 1009
prime_number = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009]

def find_max_prime(val):
    result = 0
    if val in prime_number:
        return val
    for prime in prime_number:
        if prime > math.sqrt(val):
            break
        if val % prime == 0:
            temp = max(prime, find_max_prime(int(val / prime)))
            result = max(result, temp)
            break
    if result == 0:
        return val
    else:
        return result

def find_min_starting_number(X_2):
    prev = find_max_prime(X_2)
    val = 10000000
    for i in range(X_2 - prev + 1, X_2 + 1):
        if val < i / 2 + 1:
            continue
        k = find_max_prime(i)
        if k == i:
            continue
        else:
            val = min(val, i - k + 1)
    return val
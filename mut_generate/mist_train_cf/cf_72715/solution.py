"""
QUESTION:
Write a function `count_squarefree_numbers` that takes a positive integer `N` as input and returns the total count of squarefree numbers below `2^N`. A positive integer `n` is squarefree if it is not divisible by any square of a prime number.
"""

def count_squarefree_numbers(N):
  s = list()
  cnt = [0 for _ in range(N + 1)]
 
  p = N
  while p > 0:
    s.append(p >> 1)
    p >>= 1

  f = [0 for _ in range(len(s) + 1)]
  f[1] = s[0]
 
  for i in range(2, len(s) + 1):
    f[i] = 2 * f[i - 1] + s[i - 1]

  res = N - sum(cnt[p] for p in range(2, N + 1))

  return res + f[len(s)]
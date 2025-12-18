"""
QUESTION:
Write a function `triangle(p)` that calculates the number of barely acute triangles with a perimeter not exceeding `p`, where a barely acute triangle is defined as a triangle with sides `a ≤ b ≤ c` that satisfies the condition `a^2 + b^2 = c^2 + 1`. The function should be efficient enough to handle large values of `p`, such as `25,000,000`.
"""

def triangle(p):
     mlimit = int((p / 2) ** 0.5)
     result = 0
     for m in range(2, mlimit + 1):
         if m % 2 == 0:
             start = 1
         else:
             start = 2
         for n in range(start, min(m, int((p - 2 * m * m) / (2 * m))) + 1, 2):
             a = m * m - n * n
             if a > 0:
                 result += 1
     return result
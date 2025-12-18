"""
QUESTION:
## Your Job

  Find the sum of all multiples of `n` below `m` 
  
  
## Keep in Mind

  * `n` and `m` are natural numbers (positive integers)
  * `m` is **excluded** from the multiples
  
  
## Examples
"""

def sum_of_multiples(n, m):
    if m > 0 and n > 0:
        return sum(range(n, m, n))
    else:
        return 'INVALID'
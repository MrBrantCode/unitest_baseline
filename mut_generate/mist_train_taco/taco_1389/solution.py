"""
QUESTION:
Let's say we have a number, `num`. Find the number of values of `n` such that: there exists `n` consecutive **positive** values that sum up to `num`. A positive number is `> 0`. `n` can also be 1.

```python
#Examples
num = 1
#1
return 1

num = 15
#15, (7, 8), (4, 5, 6), (1, 2, 3, 4, 5)
return 4

num = 48
#48, (15, 16, 17)
return 2

num = 97
#97, (48, 49)
return 2
```
The upper limit is `$10^8$`
"""

def count_consecutive_sum_solutions(num):
    upper_limit = 1
    while True:
        if upper_limit * (upper_limit + 1) // 2 > num:
            break
        upper_limit += 1
    
    return sum([1 if i % 2 and (not num % i) else 1 if not i % 2 and num % i == i // 2 else 0 for i in range(1, upper_limit)])
"""
QUESTION:
Write a function that takes an integer and returns an array `[A, B, C]`, where `A` is the number of multiples of 3 (but not 5) below the given integer, `B` is the number of multiples of 5 (but not 3) below the given integer and `C` is the number of multiples of 3 and 5 below the given integer. 

For example, `solution(20)` should return `[5, 2, 1]`

~~~if:r
```r
# in R, returns a numeric vector
solution(20)
[1] 5 2 1

class(solution(20))
[1] "numeric"
```
~~~
"""

def count_multiples(number):
    A = (number - 1) // 3
    B = (number - 1) // 5
    C = (number - 1) // 15
    return [A - C, B - C, C]
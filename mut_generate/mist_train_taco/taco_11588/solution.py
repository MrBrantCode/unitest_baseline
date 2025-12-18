"""
QUESTION:
In his publication Liber Abaci Leonardo Bonacci, aka Fibonacci, posed a problem involving a population of idealized rabbits. These rabbits bred at a fixed rate, matured over the course of one month, had unlimited resources, and were immortal.

Beginning with one immature pair of these idealized rabbits that produce b pairs of offspring at the end of each month. Create a function that determines the number of pair of mature rabbits after n months.

To illustrate the problem, consider the following example:

```python
fib_rabbits(5, 3) returns 19
```




Month
Immature Pairs
Adult Pairs




0
1
0


1
0
1


2
3
1


3
3
4


4
12
7


5
21
19



                                
        
Hint: any Fibonacci number can be computed using the following equation Fn = F(n-1) + F(n-2)
"""

def calculate_mature_rabbit_pairs(n, b):
    immature_pairs = 1
    mature_pairs = 0
    
    for month in range(n):
        new_immature_pairs = mature_pairs * b
        new_mature_pairs = mature_pairs + immature_pairs
        
        immature_pairs = new_immature_pairs
        mature_pairs = new_mature_pairs
    
    return mature_pairs
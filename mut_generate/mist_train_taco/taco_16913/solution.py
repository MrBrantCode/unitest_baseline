"""
QUESTION:
We need a function (for commercial purposes) that may perform integer partitions with some constraints.
The function should select how many elements each partition should have.
The function should discard some "forbidden" values in each partition.
So, create ```part_const()```, that receives three arguments.
```part_const((1), (2), (3))```
```
(1) - The integer to be partitioned

(2) - The number of elements that each partition should have

(3) - The "forbidden" element that cannot appear in any partition
```
```part_const()``` should output the amount of different integer partitions with the constraints required.

Let's see some cases:
```python
part_const(10, 3, 2) ------> 4 

/// we may have a total of 8 partitions of three elements (of course, the sum of the elements of each partition should be equal 10) :
[1, 1, 8], [1, 2, 7], [1, 3, 6], [1, 4, 5], [2, 2, 6], [2, 3, 5], [2, 4, 4], [3, 3, 4]

but 2 is the forbidden element, so we have to discard [1, 2, 7], [2, 2, 6], [2, 3, 5] and [2, 4, 4] 

So the obtained partitions of three elements without having 2 in them are:
[1, 1, 8], [1, 3, 6], [1, 4, 5] and [3, 3, 4] (4 partitions)///
```

```part_const()``` should have a particular feature:

 if we introduce ```0``` as the forbidden element, we will obtain the total amount of partitions with the constrained number of elements.

In fact, 
```python
part_const(10, 3, 0) ------> 8 # The same eight partitions that we saw above.
```

Enjoy it and happy coding!!
"""

def count_partitions_with_constraints(total_sum, partition_size, forbidden_value):
    def generate_partitions(t, k, n, l=1):
        if t < l:
            return
        elif k == 1 and t != n:
            yield [t]
        else:
            yield from ([m] + s for m in range(l, t - l + 1) for s in generate_partitions(t - m, k - 1, n, m) if m != n)
    
    return sum((1 for _ in generate_partitions(total_sum, partition_size, forbidden_value)))
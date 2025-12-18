"""
QUESTION:
Given a certain integer  ```n, n > 0```and a number of partitions,  ```k, k > 0```; we want to know the partition which has the maximum or minimum product of its terms.

The function ```find_spec_partition() ```, will receive three arguments,  ```n```,  ```k```, and a command:  ```'max' or 'min'```

The function should output the partition that has maximum or minimum value product (it depends on the given command) as an array with its terms in decreasing order.

Let's see some cases (Python and Ruby)
```
find_spec_partition(10, 4, 'max') == [3, 3, 2, 2]
find_spec_partition(10, 4, 'min') == [7, 1, 1, 1]
```
and Javascript:
```
findSpecPartition(10, 4, 'max') == [3, 3, 2, 2]
findSpecPartition(10, 4, 'min') == [7, 1, 1, 1]
```
The partitions of 10 with 4 terms with their products are:
```
(4, 3, 2, 1): 24
(4, 2, 2, 2): 32
(6, 2, 1, 1): 12
(3, 3, 3, 1): 27
(4, 4, 1, 1): 16
(5, 2, 2, 1): 20 
(7, 1, 1, 1): 7   <------- min. productvalue
(3, 3, 2, 2): 36  <------- max.product value
(5, 3, 1, 1): 15
```
Enjoy it!
"""

def find_spec_partition(n, k, com):
    """
    Finds the partition of integer `n` into `k` parts that has either the maximum or minimum product of its terms.

    Parameters:
    - n (int): The integer to be partitioned.
    - k (int): The number of partitions.
    - com (str): The command indicating whether to find the partition with the maximum ('max') or minimum ('min') product of its terms.

    Returns:
    - list: A list of integers representing the partition with the specified product property.
    """
    (x, r) = divmod(n, k)
    if com == 'max':
        return [x + 1] * r + [x] * (k - r)
    elif com == 'min':
        return [n + 1 - k] + [1] * (k - 1)
    else:
        raise ValueError("Invalid command. Use 'max' or 'min'.")
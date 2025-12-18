"""
QUESTION:
There is an integer array $\boldsymbol{d}$ which does not contain more than two elements of the same value. How many distinct ascending triples ($d[i]<d[j]<d[k],i<j<k$) are present? 

Input format 

The first line contains an integer, $N$, denoting the number of elements in the array. This is followed by a single line, containing $N$ space-separated integers. Please note that there are no leading spaces before the first number, and there are no trailing spaces after the last number.

Output format: 

A single integer that denotes the number of distinct ascending triplets present in the array.

Constraints: 

$N\leq10^5$ 

Every element of the array is present at most twice. 

Every element of the array is a 32-bit non-negative integer.

Sample input:  

6  
1 1 2 2 3 4  

Sample output:  

4

Explanation 

The distinct triplets are 

(1,2,3) 

(1,2,4) 

(1,3,4) 

(2,3,4)

The elements of the array might not be sorted. Make no assumptions of the same.
"""

def count_distinct_ascending_triplets(input_array):
    """
    Counts the number of distinct ascending triplets (d[i] < d[j] < d[k], i < j < k) in the given array.

    Parameters:
    input_array (list of int): The array of integers.

    Returns:
    int: The number of distinct ascending triplets.
    """
    root = 1
    last_level = 262144
    tree_1 = [0 for _ in range(last_level * 2 + 1)]
    tree_2 = [0 for _ in range(last_level * 2 + 1)]
    tri = [0 for _ in range(100048)]

    def less_than(x, tab):
        index = root
        sum = 0
        c_level = last_level
        while index < x + last_level:
            if x < c_level // 2:
                index *= 2
            else:
                index *= 2
                sum += tab[index]
                index += 1
                x -= c_level // 2
            c_level //= 2
        return sum

    def add_elem_1(x):
        tree = tree_1
        index = x + last_level
        tree[index] = 1
        index //= 2
        while index > 0:
            tree[index] = tree[2 * index] + tree[2 * index + 1]
            index //= 2

    def add_elem_2(x):
        tree = tree_2
        index = x + last_level
        tree[index] = less_than(x, tree_1)
        index //= 2
        while index > 0:
            tree[index] = tree[2 * index] + tree[2 * index + 1]
            index //= 2

    for i in input_array:
        add_elem_1(i)
        add_elem_2(i)
        tri[i] = less_than(i, tree_2)

    sum = 0
    for i in tri:
        sum += i

    return sum
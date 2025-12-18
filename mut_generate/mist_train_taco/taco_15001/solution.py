"""
QUESTION:
You are given $n$ elements numbered from $1$ to $n$, the element $i$ has value $a_i$ and color $c_i$, initially, $c_i = 0$ for all $i$.

The following operation can be applied:

Select three elements $i$, $j$ and $k$ ($1 \leq i < j < k \leq n$), such that $c_i$, $c_j$ and $c_k$ are all equal to $0$ and $a_i = a_k$, then set $c_j = 1$.

Find the maximum value of $\sum\limits_{i=1}^n{c_i}$ that can be obtained after applying the given operation any number of times.


-----Input-----

The first line contains an integer $n$ ($3 \leq n \leq 2 \cdot 10^5$) — the number of elements.

The second line consists of $n$ integers $a_1, a_2, \dots, a_n$ ($1 \leq a_i \leq n$), where $a_i$ is the value of the $i$-th element.


-----Output-----

Print a single integer in a line — the maximum value of $\sum\limits_{i=1}^n{c_i}$ that can be obtained after applying the given operation any number of times.


-----Examples-----

Input
7
1 2 1 2 7 4 7
Output
2
Input
13
1 2 3 2 1 3 3 4 5 5 5 4 7
Output
7


-----Note-----

In the first test, it is possible to apply the following operations in order:
"""

def max_color_sum(n, a):
    # Create a dictionary to store the last occurrence index of each value
    last_occurrence = {x: i for i, x in enumerate(a)}
    
    # Initialize variables
    max_last_index = 0
    current_last_index = 0
    color_sum = 0
    
    # Iterate through the list of values
    for i, x in enumerate(a):
        # Update the maximum last index seen so far
        max_last_index = max(max_last_index, last_occurrence[x])
        
        # If the current index is less than the last index of the current value,
        # it means we can apply the operation and increment the color sum
        if current_last_index > i:
            color_sum += 1
        else:
            # Update the current last index to the maximum last index seen so far
            current_last_index = max_last_index
    
    return color_sum
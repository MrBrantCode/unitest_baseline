"""
QUESTION:
Amr loves Chemistry, and specially doing experiments. He is preparing for a new interesting experiment.

Amr has n different types of chemicals. Each chemical i has an initial volume of a_{i} liters. For this experiment, Amr has to mix all the chemicals together, but all the chemicals volumes must be equal first. So his task is to make all the chemicals volumes equal.

To do this, Amr can do two different kind of operations.   Choose some chemical i and double its current volume so the new volume will be 2a_{i}  Choose some chemical i and divide its volume by two (integer division) so the new volume will be $\lfloor \frac{a_{i}}{2} \rfloor$ 

Suppose that each chemical is contained in a vessel of infinite volume. Now Amr wonders what is the minimum number of operations required to make all the chemicals volumes equal?


-----Input-----

The first line contains one number n (1 ≤ n ≤ 10^5), the number of chemicals.

The second line contains n space separated integers a_{i} (1 ≤ a_{i} ≤ 10^5), representing the initial volume of the i-th chemical in liters.


-----Output-----

Output one integer the minimum number of operations required to make all the chemicals volumes equal.


-----Examples-----
Input
3
4 8 2

Output
2
Input
3
3 5 6

Output
5


-----Note-----

In the first sample test, the optimal solution is to divide the second chemical volume by two, and multiply the third chemical volume by two to make all the volumes equal 4.

In the second sample test, the optimal solution is to divide the first chemical volume by two, and divide the second and the third chemical volumes by two twice to make all the volumes equal 1.
"""

def minimum_operations_to_equalize_chemicals(n, volumes):
    # Convert each volume to its binary representation and strip the '0b' prefix
    binary_representations = [bin(volume)[2:] for volume in volumes]
    
    # Get the lengths of the binary representations
    lengths = [len(binary_rep) for binary_rep in binary_representations]
    
    # Find the maximum and minimum lengths of the binary representations
    max_len = max(lengths)
    min_len = min(lengths)
    
    # Initialize the location and flag for checking common prefix
    loc = 0
    flag = False
    
    # Find the longest common prefix in the binary representations
    for j in range(min_len):
        for i in range(n):
            if binary_representations[i][j] != binary_representations[0][j]:
                flag = True
                break
        if flag:
            break
        loc += 1
    
    # Calculate the initial result based on the common prefix
    result = sum(lengths) - loc * n
    best = result
    
    # Initialize a list to track changes needed for each chemical
    change = [0] * n
    
    # Iterate over the remaining bits to calculate the minimum operations
    for j in range(loc, max_len):
        for i in range(n):
            if j >= lengths[i] or binary_representations[i][j] == '1':
                change[i] = 1
        result += sum(change)
        if result > best:
            break
        best = result
    
    return best
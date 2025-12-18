"""
QUESTION:
problem

Given a sequence of n integers a1, a2, ..., an and a positive integer k (1 ≤ k ≤ n), then the sum of k consecutive integers Si = ai + ai + Create a program that outputs the maximum value of 1 + ... + ai + k-1 (1 ≤ i ≤ n --k + 1).



input

The input consists of multiple datasets. Each dataset is given in the following format. The input ends on a line containing two zeros.

On the first line, the positive integer n (1 ≤ n ≤ 100000) and the positive integer k (1 ≤ k ≤ n) are written in this order, separated by blanks. The first + i lines after the second line. (1 ≤ i ≤ n) contains the i-th term ai (-10000 ≤ ai ≤ 10000) in the sequence. Of the scoring data, 60% of the points are n ≤ 5000, k ≤ 1000. Meet.

The number of datasets does not exceed 5.

output

The maximum value of Si is output to one line for each data set.

Examples

Input

5 3
2
5
-4
10
3
0 0


Output

11


Input

None


Output

None
"""

def find_max_sum_of_k_consecutive_elements(n, k, sequence):
    if n == 0 or k == 0 or k > n:
        return None
    
    # Calculate the initial sum of the first k elements
    current_sum = sum(sequence[0:k])
    max_sum = current_sum
    
    # Slide the window over the sequence
    for i in range(k, n):
        current_sum = current_sum + sequence[i] - sequence[i - k]
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum
"""
QUESTION:
Jeff's friends know full well that the boy likes to get sequences and arrays for his birthday. Thus, Jeff got sequence p_1, p_2, ..., p_{n} for his birthday.

Jeff hates inversions in sequences. An inversion in sequence a_1, a_2, ..., a_{n} is a pair of indexes i, j (1 ≤ i < j ≤ n), such that an inequality a_{i} > a_{j} holds.

Jeff can multiply some numbers of the sequence p by -1. At that, he wants the number of inversions in the sequence to be minimum. Help Jeff and find the minimum number of inversions he manages to get.


-----Input-----

The first line contains integer n (1 ≤ n ≤ 2000). The next line contains n integers — sequence p_1, p_2, ..., p_{n} (|p_{i}| ≤ 10^5). The numbers are separated by spaces.


-----Output-----

In a single line print the answer to the problem — the minimum number of inversions Jeff can get.


-----Examples-----
Input
2
2 1

Output
0

Input
9
-2 0 -1 0 -1 2 1 0 -1

Output
6
"""

def minimize_inversions(n, sequence):
    # Convert all elements to their absolute values
    seq = [abs(int(x)) for x in sequence]
    
    # Find the maximum value in the sequence
    Max = max(seq)
    
    # Initialize auxiliary arrays
    nxt = [0] * n
    cnt = [0] * n
    pos = [n] * (Max + 1)
    
    # Fill the pos and nxt arrays
    for i in range(n - 1, -1, -1):
        nxt[i] = pos[seq[i]]
        pos[seq[i]] = i
    
    # Process each unique value in the sequence
    for i in range(0, Max + 1):
        j = pos[i]
        while j < n:
            front = sum(cnt[0:j])
            back = sum(cnt[j + 1:n])
            if front < back:
                seq[j] = 0 - seq[j]
            j = nxt[j]
    
    # Update the cnt array
    for i in range(0, Max + 1):
        j = pos[i]
        while j < n:
            cnt[j] = 1
            j = nxt[j]
    
    # Calculate the minimum number of inversions
    inv = 0
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                inv += 1
    
    return inv